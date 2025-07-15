.PHONY: train evaluate deploy clean update-branch



train:
	python src/train_pipeline.py

# evaluate:
# 	python src/evaluate.py



clean:
	rm -rf models/*.skops results/*.csv results/*.png

update-branch:
	git config --global user.name ${USER_NAME}
	git config --global user.email ${USER_EMAIL}
	git remote set-url origin https://${TOKEN}@github.com/${REPO}.git
	git commit -am "Update branch" || echo "Nothing to commit"
	git push --force origin HEAD:update

hf-login:
	git config --global user.name "${USER_NAME}"
	git config --global user.email "${USER_EMAIL}"
	git switch update
	git pull origin update --allow-unrelated-histories
	pip install -U "huggingface_hub[cli]"
	git config --global credential.helper store
	huggingface-cli login --token ${HF} --add-to-git-credential

push-hub:
	# Bersihkan jika folder sudah ada
	rm -rf huggingface-space

	# Clone dari Hugging Face Space
	git clone https://huggingface.co/spaces/FaizKhalifah/tugasmlops huggingface-space

	# Siapkan struktur direktori
	mkdir -p huggingface-space/models huggingface-space/results huggingface-space/data

	# Salin file aplikasi
	cp -r app/* huggingface-space/
	cp requirements.txt huggingface-space/

	# Masuk ke folder dan siapkan DVC
	cd huggingface-space && \
	git config user.name "${USER_NAME}" && \
	git config user.email "${USER_EMAIL}" && \
	dvc init --no-scm && \
	dvc remote add -d dagshub https://dagshub.com/FaizKhalifah/tugasmlops-storage.dvc && \
	dvc remote modify dagshub --local auth basic && \
	dvc remote modify dagshub --local user "${DAGSHUB_USER}" && \
	dvc remote modify dagshub --local password "${DAGSHUB_TOKEN}" && \
	dvc pull

	# Lanjutkan git LFS
	cd huggingface-space && \
	git lfs install && \
	git lfs track "*.skops" "*.png" "*.csv" && \
	git add .gitattributes

	# Tambahkan dan push ke HF
	cd huggingface-space && \
	git add . && \
	git commit -m "Update space with data & models from DVC" || echo "Nothing to commit" && \
	git push origin main



deploy: hf-login push-hub
