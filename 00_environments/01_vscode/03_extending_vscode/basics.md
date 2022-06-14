# Extending Workbench
<tag>- Ref: https://code.visualstudio.com/api/extension-capabilities/extending-workbench</tag>

"Workbench" refers to the overall Visual Studio Code UI that encompasses the following UI components:

- Title Bar
- Activity Bar
- Side Bar
- Panel
- Editor Group
- Status Bar

VS Code provides various APIs that allow you to add your own components to the Workbench. For example, in the image below:


## Customize Outline View (Hack)
<!-- HK: Inject CSS and JS to VSCode GUI -->

1. `Help` -> `Toggle Developer Tools`
2. Observe the html elements and the styles of the outline item
3. Install [Custom CSS & JS Extension](https://github.com/be5invis/vscode-custom-css) that can inject CSS to VSCode GUI
4. Create a new style.css with the styles required.
5. Alternatively, can create a javascript.js to apply styles dynamically.

<!-- TODO: Test the code below thoroughly. -->
```javascript
var colors = {
    "1": "#a685e4",
    "2": "#b7b7fa",
    "3": "#d1ddf5",
    "4": "#9BCFE0"
};

document.addEventListener("DOMContentLoaded", function() {

    // Handle `DOMSubtreeModified` event to `body` element first.
    // Initially, "outline-tree" element is not rendered when VSCode loads the GUI.
    const bodyElement = document.getElementsByTagName("body")[0];
    bodyElement.addEventListener("DOMSubtreeModified", bodyModified);

    function outlineTreeModified(e) {  

        // Modify the outline view only for markdown files      
        if (document.title.includes(".md"))
        {
            if (e.target.className == 'monaco-list-row')
            {
                level = e.target.getAttribute('aria-level');
                if (level)  // if not null
                    e.target.style = "color: " + colors[level];
            }
        }
        
    }

    function bodyModified(e) {

        const collection = document.getElementsByClassName("outline-tree");
        
        // When "outline-tree" element becomes available
        if (collection)
        {
            // Handle `DOMSubtreeModified` event
            collection[0].addEventListener("DOMSubtreeModified", outlineTreeModified);

            // PERF: Remove the event handler from `body` element
            element.removeEventListener("DOMSubtreeModified", bodyModified);
        }
    }
});
```

6. Add following to the `settings.json`:
```yaml
"vscode_custom_css.imports": ["file:///C:/Users/chath/.test/style.css", "file:///C:/Users/chath/.test/javascript.js"]

// URIs must be used.

```

### Custom CSS & JS Extension
<tag>- Ref: https://marketplace.visualstudio.com/items?itemName=be5invis.vscode-custom-css</tag>

> <note>❗️ Important: If Visual Studio Code complains about that it is corrupted, simply click “Don't show again”.</note>

> <note>Every time after Visual Studio Code is updated, please re-enable Custom CSS.</note>

> <note>Every time you change the configuration, please re-enable Custom CSS.</note>


#### VSCode Extension to Fix Checksums

An extension to to adjust checksums after changes to VSCode core files. Once the checksum changes are applied and VSCode is restarted, all warning about core file modifications will disappear, such as the display of [Unsupported] in the title-bar, or the following dialog on start-up:

<ext>Fix VSCode Checksums Extension</ext>\
<tag>- Ref: https://marketplace.visualstudio.com/items?itemName=lehni.vscode-fix-checksums</tag>