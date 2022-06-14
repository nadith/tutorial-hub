#%%
# Todo Tree Extension Usage
# ------------------------- 

# ! BG: This is a bug
# ! BUG This is a bug
# ! next line
# TD: This is a TODO
# TODO: This is a TODO
# ? ST: This is a study note
# ? STUDY: This is a study note
# ? next line
# FX: This is a to fix
# FIX: This is a to fix
# HK: This is a HACK
# HACK: This is a HACK
# DP: This is deprecated
# DEPRECATED: This is deprecated
# * IM: This is IMPORTANT
# * IMPORTANT: This is important text
# * next line


# Todo Tree Plugin:
# https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree

# todo-tree.highlights.useColourScheme (false)
# Use a simple scheme for colouring highlights. This will simply apply a list of colours in the same order as the tags are defined. Use this as a much simpler alternative to setting up custom highlights for each tag.

# Note: The colour scheme overrides the colours defined in todo-tree.highlights.defaultHighlight but not todo-tree.highlights.customHighlight.

# todo-tree.highlights.backgroundColourScheme (["red","orange","yellow","green","blue","indigo","violet"])
# Defines colours for use in conjunction with todo-tree.highlights.useColourScheme to colour highlights. Colours can be defined in the same way as other colours (e.g. hex code, theme names, etc.). If there are more tags than colours, the sequence is repeated.

# todo-tree.highlights.foreroundColourScheme (["white","black","black","white","white","white","black"])
# Defines colours for use in conjunction with todo-tree.highlights.backgroundColourScheme to colour highlights. These colours should be complementary to the background colours.

# todo-tree.general.tagGroups ({})
# This setting allows multiple tags to be treated as a single group. Example:

#     "todo-tree.general.tagGroups": {
#         "FIXME": [
#             "FIXME",
#             "FIXIT",
#             "FIX",
#         ]
#     },
# This treats any of FIXME, FIXIT or FIX as FIXME. When the tree is grouped by tag, all of these will appear under the FIXME node. This also means that custom highlights are applied to the group, not each tag type.

# Highlighting
# New!: If you just want to set different colours for tags, you can now enable todo-tree.highlights.useColourScheme. This will apply a set of colours (which can be changed) to the tags in the order that they are defined.

# Highlighting tags is configurable. Use defaultHighlight to set up highlights for all tags. If you need to configure individual tags differently, use customHighlight. If settings are not specified in customHighlight, the value from defaultHighlight is used.

# Custom highlights can also be specified for sub tags (if used).

# Note: defaultHighlight is not applied to sub tags.

# Both defaultHighlight and customHighlight allow for the following settings:

# foreground - used to set the foreground colour of the highlight in the editor and the marker in the ruler.

# background - used to set the background colour of the highlight in the editor.

# Note: Foreground and background colours can be specified using HTML/CSS colour names (e.g. "Salmon"), RGB hex values (e.g. "#80FF00"), RGB CSS style values (e.g. "rgb(255,128,0)" or colours from the current theme, e.g. peekViewResult.background. See Theme Color for the details. Hex and RGB values can also have an alpha specified, e.g. "#ff800080" or "rgba(255,128,0,0.5)".

# opacity - percentage value used with the background colour. 100% will produce an opaque background which will obscure selection and other decorations.

# Note: opacity can only be specified when hex or RGB colours are used.

# fontWeight, fontStyle, textDecoration - can be used to style the highlight with standard CSS values.

# borderRadius - used to set the border radius of the background of the highlight.

# icon - used to set a different icon in the tree view. Must be a valid octicon (see https://octicons.github.com) or codicon (see https://microsoft.github.io/vscode-codicons/dist/codicon.html). If using codicons, specify them in the format "$(icon)". The icon defaults to a tick if it's not valid. You can also use "todo-tree", or "todo-tree-filled" if you want to use the icon from the activity view.

# iconColour - used to set the colour of the icon in the tree. If not specified, it will try to use the foreground colour or the background colour. Colour can be specified as per foreground and background colours, but see note below.

# Note: Theme colours are only supported when using codicons. Hex, RGB and HTML colours are only supported when using octicons or the default icon.

# gutterIcon - set to true to show the icon in the editor gutter.

# Note: Unfortunately, only octicons and the todo-tree icon can be displayed in the gutter.

# rulerColour - used to set the colour of the marker in the overview ruler. If not specified, 
# it will default to use the foreground colour. Colour can be specified as per foreground and 
# background colours.

# rulerOpacity - used to set the opacity of the ruler markers.

# Note: Only works with hex and RGB colour settings.

# rulerLane - used to set the lane for the marker in the overview ruler. If not specified, 
# it will default to the right hand lane. Use one of "left", "center", "right", or "full". 
# You can also use "none" to disable the ruler markers.

# type - used to control how much is highlighted in the editor. Valid values are:

# tag - highlights just the tag
# text - highlights the tag and any text after the tag
# tag-and-comment - highlights the comment characters (or the start of the match) and the tag
# tag-and-subTag - as above, but allows the sub tag to be highlight too (with colours defined in custom highlights)
# text-and-comment - highlights the comment characters (or the start of the match), the tag and the text after the tag
# line - highlights the entire line containing the tag
# whole-line - highlights the entire line containing the tag to the full width of the editor
# capture-groups:n,m... - highlights capture groups from the regex, where 'n' is the index into the regex
# none - disable highlightling in the document
# hideFromTree - used to hide tags from the tree, but still highlight in files

# hideFromStatusBar - prevents the tag from being included in the status bar counts

# Example:

# "todo-tree.highlights.defaultHighlight": {
#     "icon": "alert",
#     "type": "text",
#     "foreground": "red",
#     "background": "white",
#     "opacity": 50,
#     "iconColour": "blue"
# },
# "todo-tree.highlights.customHighlight": {
#     "TODO": {
#         "icon": "check",
#         "type": "line"
#     },
#     "FIXME": {
#         "foreground": "black",
#         "iconColour": "yellow",
#         "gutterIcon": true
#     }
# }
# Note: The highlight configuration is separate from the settings for the search. Adding settings in customHighlight does not automatically add the tags into todo-tree.general.tags.

# *Note: Using the capture-groups setting in type may have an impact on performance with large files.

# todo-tree.regex.subTagRegex 
# This is a regular expression for processing the text to the right of the tag, e.g. 
# for extracting a sub tag, or removing unwanted characters. Anything that 
# the regex matches will be removed from the text. If a capture group is included, 
# the contents are extracted into a sub tag, which will be used in the tree to group similar tags. 
# The sub tag can also be used as a placeholder in todo-tree.tree.subTagClickUrl 
# and todo-tree.tree.labelFormat. Sub tags can also be highlighted by specifying a 
# section in the todo-tree.highlights.customHighlights setting. To highlight the sub 
# tag itself, set "type" to "tag-and-subTag" in custom highlights for the tag.

# todo-tree.regex.regexCaseSensitive (true)
# Set to false to allow tags to be matched regardless of case.