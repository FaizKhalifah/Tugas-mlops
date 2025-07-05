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
	git pull origin update
	git switch update
	pip install -U "huggingface_hub[cli]"
	huggingface-cli login --token ${HF} --add-to-git-credential

push-hub:
	huggingface-cli repo upload FaizKhalifah/tugasmlops ./app/app.py --repo-type=space --commit-message "Update app"
	huggingface-cli repo upload FaizKhalifah/tugasmlops ./models/Logistic Regression.skops --repo-type=space --commit-message "Upload model"
	huggingface-cli repo upload FaizKhalifah/tugasmlops ./results/matrix/confusion_matrix_Logistic Regression.png --repo-type=space --commit-message "Upload result"

deploy: hf-login push-hub
