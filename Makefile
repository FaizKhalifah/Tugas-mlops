# 225150207111069_Raihan Fadhillah Baihaqi 			
# 225150207111075_Hernando Atha 				
# 225150207111066_Muhammad Alfaiz Khalifah Alamsyah 	
# 225150200111034_Qyan Rommy Mario				
# 225150201111029_Davin Dalana Fidelio Fredra	

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
	# Bersihkan folder jika sudah ada
	rm -rf huggingface-space

	# Clone dari Hugging Face Space
	git clone https://huggingface.co/spaces/FaizKhalifah/tugasmlops huggingface-space

	# Buat direktori jika belum ada
	mkdir -p huggingface-space/models huggingface-space/results huggingface-space/data

	

	# Konfigurasi DVC di dalam Hugging Face space
	cd huggingface-space && \
	dvc init --no-scm && \
	dvc remote add -d origin s3://dvc && \
	dvc remote modify origin endpointurl https://dagshub.com/FaizKhalifah/Tugas-mlops.s3 && \
	dvc remote modify origin --local access_key_id ${DAGSHUB_KEY} && \
	dvc remote modify origin --local secret_access_key ${DAGSHUB_SECRET} && \
	dvc pull

	# Salin semua file project (app, models, dvc metadata)
	cp -r app/* huggingface-space/
	cp requirements.txt huggingface-space/

	# Git LFS setup
	cd huggingface-space && \
	git config user.name "${USER_NAME}" && \
	git config user.email "${USER_EMAIL}" && \
	git lfs install && \
	git lfs track "*.skops" "*.png" "*.csv" && \
	git add .gitattributes

	# Git commit & push
	cd huggingface-space && \
	git add . && \
	git commit -m "Update with DVC S3 pull from DagsHub" || echo "Nothing to commit" && \
	git push origin main


deploy: hf-login push-hub
