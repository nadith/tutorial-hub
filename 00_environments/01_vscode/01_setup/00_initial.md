# Setting up VSCode

## 1. Install VSCode

Download VSCode via [link.](https://code.visualstudio.com/download)

## 2. [optional] Login to microsoft or Github via VSCode to enable native settings sync

Once logged in to the microsoft or github account, the `settings.json` will be synced provided that you login to the same account in the other PC.

> <note>❗️ Important: Unfortunately this will not sync installed extensions.</note>

## 3. Install & Use <ext>Settings Sync Extension</ext>
<tag>- Ref: https://dev.to/shanalikhan/visual-studio-code-settings-sync-configurations-mn0</tag>

Configure it according to `<link>`
- Can sync all files that native VSCode sync supports
- Can sync installed extensions
- Can sync custom files (i.e. user's dictionary files, etc)

## 4. Install Anaconda (python environment)

[Download anaconda](https://www.anaconda.com/products/distribution) and install it. Anaconda comes with: 

- `numpy` package (numerical python - vectors, matrixes, etc.)
- `skikit-learn `package (machine learning)
- `jupyter` package (interactive python notebooks)
- `matplotlib` package (plotting in python)

### 4.1 Set `PYTHONPATH` Environment Variable <o>(important)</o>

Set `PYTHONPATH` to the code base to avoid `module not found` errors.

### 4.2 Install packages listed in `00_install.ipynb`

Install the packages listed in [00_install.ipynb](00_install.ipynb)

