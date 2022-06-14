# <r2>0. CAUTION: Before Installing/Reinstalling Anaconda</r2>

Following folders/destinations will be removed with Anaconda uninstallation.

**Make sure to backup:**
- All the `bookmark files` in each `.vscode` folder in package folders (i.e. `fastai`, `wandb`, `tensorflow`, `pytorch`).
- All `line note files` (from <ext>Line Note Extension</ext>) in each `.vscode` folder in package folders (i.e. `fastai`, `wandb`, `tensorflow`, `pytorch`).

# 1. VSCode Related Files

In general, all files in `.vscode` folder.


VSCode native sync will sync the following files:

- Settings.json
- Keyboard Shortcuts for each platform
- User Snippets
- User Tasks
- Extensions
- UI State

Use <ext>Setting Sync Extension:</ext>

> <note><ext>Setting Sync Extension</ext>, by default syncs `C:\Users\<user>\AppData\Roaming\Code\User` folder.</note>

Configure custom files to sync or ignore files by editing the **global configuration:**

`> Sync: Advanced Options -> Sync: Edit Extension Local Settings`

File:\
`C:\Users\<user>\AppData\Roaming\Code\User\syncLocalSettings.json`


# 2. VCode Extension Related Files

## <ext>2.1 Bookmarks Extension</ext> 

All bookmark files in `.vscode folder` for each project or reference libraries (i.e. `fastai`, etc).

## <ext>2.2 Line Notes Extension</ext>

All line notes in `.vscode folder` for each project or reference libraries (i.e. `fastai`, etc). 

## <ext>2.2 Markdown Preview Enhanced Extension</ext>

**Custom Style Sheet:**\
`C:\Users\chath\.mume\style.less` 

**Other Files:**\
`C:\Users\chath\.mume`

## <ext>2.2 Code Spell Checker Extension</ext>

**Custom Dictionary Files**\
`C:\Users\chath\.cspell`

# 2. Other Important Files

## 2.1 Public / Private Key Files

Useful for GitHub Authentication:
`C:\Users\chath\.ssh `

## 2.2 Config Files:
`C:\Users\chath\.config\git`\
`C:\Users\chath\.config\wandb`

## 2.3 Take the installed extension list to a file (in case)

In windows power shell,

```shell
PS C:\Users\chath> code --list-extensions | % { "code --install-extension $_" }

code --install-extension aaron-bond.better-comments
code --install-extension alefragnani.Bookmarks
code --install-extension alefragnani.project-manager
code --install-extension analytic-signal.preview-mp4
code --install-extension ArturoDent.launch-config
code --install-extension Atishay-Jain.All-Autocomplete
code --install-extension bierner.markdown-mermaid
code --install-extension bpruitt-goddard.mermaid-markdown-syntax-highlighting
code --install-extension CodeStream.codestream
code --install-extension codezombiech.gitignore
code --install-extension csholmq.excel-to-markdown-table
code --install-extension dbaeumer.vscode-eslint
code --install-extension eamodio.gitlens
code --install-extension esbenp.prettier-vscode
code --install-extension evilz.vscode-reveal
code --install-extension formulahendry.auto-close-tag
code --install-extension formulahendry.auto-rename-tag
code --install-extension formulahendry.code-runner
code --install-extension gera2ld.markmap-vscode
code --install-extension GitHub.copilot
code --install-extension Gruntfuggly.todo-tree
code --install-extension IBM.output-colorizer
code --install-extension inu1255.easy-snippet
code --install-extension ionutvmi.reg
code --install-extension jasonlhy.hungry-delete
code --install-extension jebbs.plantuml
code --install-extension jeff-hykin.better-cpp-syntax
code --install-extension johnpapa.vscode-peacock
code --install-extension karigari.chat
code --install-extension KevinRose.vsc-python-indent
code --install-extension lacroixdavid1.vscode-format-context-menu
code --install-extension lostintangent.vsls-whiteboard
code --install-extension mhutchie.git-graph
code --install-extension mikestead.dotenv
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension ms-toolsai.jupyter-keymap
code --install-extension ms-toolsai.jupyter-renderers
code --install-extension ms-vscode-remote.remote-wsl
code --install-extension ms-vscode.cpptools-themes
code --install-extension ms-vsliveshare.vsliveshare
code --install-extension ms-vsliveshare.vsliveshare-audio
code --install-extension njpwerner.autodocstring
code --install-extension phoihos.markdown-markmap
code --install-extension PKief.material-icon-theme
code --install-extension RedVanWorkshop.explorer-exclude-vscode-extension
code --install-extension ritwickdey.LiveServer
code --install-extension Shan.code-settings-sync
code --install-extension shd101wyy.markdown-preview-enhanced
code --install-extension streetsidesoftware.code-spell-checker
code --install-extension TakumiI.markdowntable
code --install-extension techer.open-in-browser
code --install-extension thekalinga.bootstrap4-vscode
code --install-extension tkrkt.linenote
code --install-extension tomoki1207.pdf
code --install-extension travisthieman.better-search
code --install-extension VisualStudioExptTeam.vscodeintellicode
code --install-extension xdebug.php-debug
code --install-extension yzhang.markdown-all-in-one
code --install-extension ziyasal.vscode-open-in-github
code --install-extension zobo.php-intellisense
```