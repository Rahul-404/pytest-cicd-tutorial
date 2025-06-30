# 🧪 CI/CD Practice with GitHub Actions

This repository is created for hands-on practice with **CI/CD pipelines** using **GitHub Actions**. The project includes:

- ✅ Unit testing using `pytest`
- 🐍 Multi-version Python testing (3.8, 3.9, 3.10)
- 🖥️ OS matrix builds
- 🔄 Automated workflows triggered by pushes and pull requests

---

## 🚀 Tech Stack

- Python
- Pytest
- GitHub Actions (CI/CD)

---

## ⚙️ GitHub Actions Workflow

- Tests run automatically on each push or pull request.
- Matrix strategy used to test on multiple Python versions and OS environments.
- Clean separation of setup, install, and test steps.

---

## 🧪 Running Tests Locally

```bash
pip install -r requirements.txt
pytest
````

---

## 📂 Project Structure

```
.
├── .github/workflows/
│   └── ci.yml            # GitHub Actions workflow
├── tests/                # Pytest test files
├── my_module/            # Your application code
├── requirements.txt
└── README.md
```

---

## 📌 Learning Objectives

* Understand how GitHub Actions works
* Set up a Python project with automated tests
* Gain experience with version and OS testing
* Prepare for real-world CI/CD pipelines

---

## 🧠 Notes

This is a **practice repository** based on a tutorial to solidify core CI/CD concepts. It's a great foundation for production-ready DevOps integration in Python projects.

---

## 📜 License

This project is for educational purposes. Feel free to fork and experiment.
