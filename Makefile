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
	rm -rf huggingface-space
	git clone https://huggingface.co/spaces/FaizKhalifah/tugasmlops huggingface-space
	mkdir -p huggingface-space/models huggingface-space/results
	cp -r app/* huggingface-space/
	cp -r models/*.skops huggingface-space/models/
	cp -r results huggingface-space/

	cd huggingface-space && \
	git config user.name "${USER_NAME}" && \
	git config user.email "${USER_EMAIL}" && \
	git add .gitattributes && \
	git add . && \
	git lfs install && \
	git lfs track "*.skops" "*.png" "*.csv" && \
	git commit -m "Update space" || echo "Nothing to commit" && \
	git push origin main



deploy: hf-login push-hub
