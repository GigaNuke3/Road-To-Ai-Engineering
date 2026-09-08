# Learning Python Fundamentals and Basics

The model gets cached in a local folder on your machine — here's how to find and remove it.

**Check where it's stored:**
```bash
ls ~/.cache/huggingface/hub
```
You should see a folder named something like `models--sentence-transformers--all-MiniLM-L6-v2`.

**To delete just that specific model:**
```bash
rm -rf ~/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2
```

**To see how much space it's actually taking up first (good idea before deleting):**
```bash
du -sh ~/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2
```

**If you ever want to clear out ALL cached Hugging Face models (not just this one):**
```bash
rm -rf ~/.cache/huggingface
```
Careful with this one — it removes everything cached, so any other Hugging Face models you've downloaded would need to redownload next time you use them.

Worth knowing: if you delete it now but want to run the embedding script again later, it'll just automatically redownload it — no need to reinstall `sentence-transformers` itself, just the model weights get pulled again.





