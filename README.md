# Selenium Framework Starter 🚀

This is a reusable test automation framework built with **Selenium**, **Pytest**, and the **Page Object Model (POM)**. It’s designed to get you up and running quickly for web UI test automation projects.

## 🔧 Features

- ✅ Pytest test runner
- ✅ Page Object Model (POM) structure
- ✅ Centralized WebDriver setup with `conftest.py`
- ✅ Screenshot capture on test failure
- ✅ Logging with timestamped messages
- ✅ Readable, scalable test organization

## 📁 Folder Structure

```
selenium_starter/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── logs/
├── screenshots/
├── src/
│   ├── utils/
│   │   └── logger.py
│   └── pages/
│       └── sign_in_page.py
├── tests/
│   └── test_login_flow.py
└── README.md
```

## 🚀 How to Run

1. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

2. **Run the test**

To run the test suite, simply use:

```bash
pytest
```

Thanks to `pytest.ini`, no additional flags are necessary.

To run tests in **headless mode**, add the `--headless` flag when running the tests:

```bash
pytest --headless
```

This makes it easy to switch between running in a browser or silently in the background.


3. **View logs and screenshots**  
   - Logs: `logs/` folder  
   - Screenshots (on failure): `screenshots/` folder

## 🧱 Technologies Used

- Python 3.10+
- Selenium WebDriver
- Pytest
- WebDriver Manager

## 📦 How to Extend

- Add new page objects in `src/pages/`
- Write more test cases in `tests/`
- Import and reuse `logger` from `src/utils/logger.py`
- Modify `conftest.py` for headless runs, different browsers, etc.

## ✍️ Author

**Zachary Coleman**  
[GitHub](https://github.com/ZColeman8) • [LinkedIn](https://www.linkedin.com/in/zachary-coleman-4bb4a9a4/)

---

> ⚡ *This framework is designed to help you launch QA automation projects quickly. Copy, adapt, and go!*