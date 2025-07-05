.PHONY: train evaluate deploy clean update-branch



train:
	python src/train_pipeline.py

# evaluate:
# 	python src/evaluate.py

deploy:
	python app/main.py

clean:
	rm -rf models/*.skops results/*.csv results/*.png

update-branch:
	git config --global user.name ${USER_NAME}
	git config --global user.email ${USER_EMAIL}
	git remote set-url origin https://${TOKEN}@github.com/${REPO}.git
	git commit -am "Update branch" || echo "Nothing to commit"
	git push --force origin HEAD:update

hf-login:
	git pull --no-rebase origin update --allow-unrelated-histories
	git switch update
	pip install -U "huggingface_hub[cli]"
	huggingface-cli login --token ${HF} --add-to-git-credential

push-hub:
	cd huggingface-space && \
	git add . && \
	git commit -m "Update space" || echo "Nothing to commit" && \
	git push origin main


deploy: hf-login push-hub
