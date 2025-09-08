# 📁 PROJECT EXPORT FOR LLMs

## 📊 Project Information

- **Project Name**: `agentic-finlit-backend`
- **Generated On**: 2025-09-08 03:52:41 (Etc/GMT+5 / GMT-05:00)
- **Total Files Processed**: 6
- **Export Tool**: Easy Whole Project to Single Text File for LLMs v1.1.0
- **Tool Author**: Jota / José Guilherme Pandolfi

### ⚙️ Export Configuration

| Setting | Value |
|---------|-------|
| Language | `en` |
| Max File Size | `1 MB` |
| Include Hidden Files | `false` |
| Output Format | `both` |

## 🌳 Project Structure

```
├── 📁 app/
│   ├── 📄 main.py (180 B)
│   └── 📄 README.md (107 B)
├── 📄 Dockerfile (228 B)
├── 📄 elkay.txt
├── 📄 README.md (275 B)
└── 📄 requirements.txt (45 B)
```

## 📑 Table of Contents

**Project Files:**

- [📄 app/main.py](#📄-app-main-py)
- [📄 app/README.md](#📄-app-readme-md)
- [📄 elkay.txt](#📄-elkay-txt)
- [📄 README.md](#📄-readme-md)
- [📄 requirements.txt](#📄-requirements-txt)

---

## 📈 Project Statistics

| Metric | Count |
|--------|-------|
| Total Files | 6 |
| Total Directories | 1 |
| Text Files | 5 |
| Binary Files | 1 |
| Total Size | 835 B |

### 📄 File Types Distribution

| Extension | Count |
|-----------|-------|
| `.md` | 2 |
| `.txt` | 2 |
| `.py` | 1 |
| `no extension` | 1 |

## 💻 File Code Contents

### <a id="📄-app-main-py"></a>📄 `app/main.py`

**File Info:**
- **Size**: 180 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `app/main.py`
- **Relative Path**: `app`
- **Created**: 2025-09-08 03:31:10 (Etc/GMT+5 / GMT-05:00)
- **Modified**: 2025-09-08 03:31:10 (Etc/GMT+5 / GMT-05:00)
- **MD5**: `7ab713ad1423dcc3b60a557f8a8dfc2f`
- **SHA256**: `b5ef7c4b10661a2978bfb99c0f72ba60b109ffa0ac958a491083294cde6c463a`
- **Encoding**: ASCII

**File code content:**

```python
from fastapi import FastAPI

api = FastAPI(title="Agentic FinLit Backend (Starter)")

@api.get("/")
def root():
    return {"ok": True, "service": "agentic-finlit-backend"}

```

---

### <a id="📄-app-readme-md"></a>📄 `app/README.md`

**File Info:**
- **Size**: 107 B
- **Extension**: `.md`
- **Language**: `text`
- **Location**: `app/README.md`
- **Relative Path**: `app`
- **Created**: 2025-09-08 03:31:10 (Etc/GMT+5 / GMT-05:00)
- **Modified**: 2025-09-08 03:31:10 (Etc/GMT+5 / GMT-05:00)
- **MD5**: `bbd494783866d77eb7a8f3c890e23488`
- **SHA256**: `d258a946b44e462be9c71fcc99bb0b2116018423033dcd3fbc30c07d875694f6`
- **Encoding**: ASCII

**File code content:**

````markdown
# Agentic FinLit Backend (Starter)
FastAPI service for the agentic flow. Deployed on HF Spaces (Docker).

````

---

### <a id="📄-elkay-txt"></a>📄 `elkay.txt`

**File Info:**
- **Size**: 0 B
- **Extension**: `.txt`
- **Language**: `text`
- **Location**: `elkay.txt`
- **Relative Path**: `root`
- **Created**: 2025-09-08 03:52:24 (Etc/GMT+5 / GMT-05:00)
- **Modified**: 2025-09-08 03:52:24 (Etc/GMT+5 / GMT-05:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```text

```

---

### <a id="📄-readme-md"></a>📄 `README.md`

**File Info:**
- **Size**: 275 B
- **Extension**: `.md`
- **Language**: `text`
- **Location**: `README.md`
- **Relative Path**: `root`
- **Created**: 2025-09-08 03:31:10 (Etc/GMT+5 / GMT-05:00)
- **Modified**: 2025-09-08 03:31:10 (Etc/GMT+5 / GMT-05:00)
- **MD5**: `0cca3ff72cdf5cdca7fb11c3b7aa420f`
- **SHA256**: `6203dc1feff04f8cd222df2b4154cfd0f18e47c9db3ad34e98124efc01debc01`
- **Encoding**: UTF-8

**File code content:**

````markdown
---
title: Agentic Finlit Backend
emoji: 📊
colorFrom: red
colorTo: green
sdk: docker
pinned: false
license: unknown
short_description: agentic-finlit-backend
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

````

---

### <a id="📄-requirements-txt"></a>📄 `requirements.txt`

**File Info:**
- **Size**: 45 B
- **Extension**: `.txt`
- **Language**: `text`
- **Location**: `requirements.txt`
- **Relative Path**: `root`
- **Created**: 2025-09-08 03:23:55 (Etc/GMT+5 / GMT-05:00)
- **Modified**: 2025-09-08 03:31:10 (Etc/GMT+5 / GMT-05:00)
- **MD5**: `a29c654efdcaced933646b542a898012`
- **SHA256**: `bce0d135c35acc8fabbb855872efbc54e36101ae28ac738d22d55fbb6a7022c3`
- **Encoding**: ASCII

**File code content:**

```text
fastapi==0.111.0
uvicorn[standard]==0.30.1

```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `Dockerfile`

