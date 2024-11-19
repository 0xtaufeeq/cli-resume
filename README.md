# CLI Resume

So, you’re ready to take your resume game to the next level? Cool, because this CLI Resume project does just that. No boring PDFs or generic templates. This is a dynamic, animated terminal experience that screams, *“Hey, I’m not your average candidate.”*

---

## Why Build This?

Because why not? Think about it, you're a dev. Your resume can be more than a list of jobs and skills; it can *be* the proof of those skills. This project lets you showcase your achievements in a way that's functional, creative, and uniquely *you*. Plus, it’s fun to build (and even more fun to flex lol).

---

## How to Build Your Own?


### Step 1: Fork and Then Clone the Repository

Start by forking and cloning the repository and maybe drop a star ;)

```bash
git clone https://github.com/<your-username>/cli-resume.git
cd cli-resume
```


### Step 2: Install Dependencies
This project runs on Python (3.7+). Make sure you’ve got it installed, then add the required libraries 

```bash
pip install -r requirements.txt
```

### Step 3: Make It Yours

Your profile details must be added to ```resume.py```. Open it up, and update the resume content and other details to fit your story.

#### Quick Tips -

- Use [Rich Documentation](https://rich.readthedocs.io/en/stable/) for cool formatting.
- Add some personality to make it your own.Rich has a ton of formatting options.
- Keep it concise but impactful. No one wants a terminal novel.
- Add Interactivity like menus or commands.

### Step 4: Build and Test The Python Package

#### Step 4.1: Package the Library
Make sure your `setup.py` file is correctly configured, then build the package 

```bash
python setup.py sdist bdist_wheel
```

#### Step 4.2: Install the Library Locally
After building the package, you can install it locally for testing.
```bash
pip install .
```

#### Step 4.3: Run and test the Installed Library
Once installed, run the CLI tool from anywhere.

```bash
taufeeq-resume
```
Boom! Your terminal just became your resume stage. You can always change the above command to your liking.

### Step 6: Share It with the World
Want others to use your CLI resume? Upload it to PyPI (Python Package Index)

#### 1. Install Twine
```bash
pip install twine
```

#### 2. Upload the Package (You need a PyPi Account)

```bash
twine upload dist/*
```




## Contributing
If you’ve got cool ideas, submit a pull request. I’d love to see what you come up with!

### How To Contribute?
#### 1. Fork the repo.
#### 2. Create a new branch
```bash
git checkout -b an-amazing-feature
```
#### 3. Commit and Push
```bash
git add .
git commit -m "Added my awesome feature!"
git push origin my-awesome-feature
```
#### 4. Open a pull request. 🎉

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit). Feel free to use, modify, and distribute!

TLDR; do whatever you want, but don’t sue me if something goes wrong. 
