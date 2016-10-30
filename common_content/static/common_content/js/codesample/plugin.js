/*
Customized version of TinyMCE 4 codesample plugin.

It uses external Prism.js js/css components and supports all languages supported by Prism.
*/
var DOM = tinymce.dom.DOMUtils.DOM;

function wrapCode(element) {
	element.innerHTML = '<code>' + element.innerHTML + '</code>';
}

function checkLineNumbers(node) {
  var match = node.className.match(/line-numbers/);
  return match != null;
}

function isCodeSample(elm) {
	return elm && elm.nodeName == 'PRE' && elm.className.indexOf('language-') !== -1;
}

function trimArg(predicateFn) {
	return function(arg1, arg2) {
		return predicateFn(arg2);
	};
}

function getLanguages(editor) {
    var defaultLanguages = [
      {text: 'HTML/XML', value: 'markup'},
      {text: 'JavaScript', value: 'javascript'},
      {text: 'CSS', value: 'css'},
      {text: 'PHP', value: 'php'},
      {text: 'Ruby', value: 'ruby'},
      {text: 'Python', value: 'python'},
      {text: 'Java', value: 'java'},
      {text: 'C', value: 'c'},
      {text: 'C#', value: 'csharp'},
      {text: 'C++', value: 'cpp'}
    ];

	var customLanguages = editor.settings.codesample_languages;
	return customLanguages ? customLanguages : defaultLanguages;
}

function insertCodeSample(editor, language, code, checked) {
	editor.undoManager.transact(function() {
		var node = getSelectedCodeSample(editor);

    var line_numbers = '';
    if (checked) {
      line_numbers = ' line-numbers';
    }

		code = DOM.encode(code);

		if (node) {
			editor.dom.setAttrib(node, 'class', 'language-' + language + line_numbers);
			node.innerHTML = code;
      wrapCode(node);
      Prism.highlightElement(node.firstChild);
			editor.selection.select(node);
		} else {
			editor.insertContent('<pre id="__new" class="language-' + language + line_numbers + '">' + code + '</pre>');
			editor.selection.select(editor.$('#__new').removeAttr('id')[0]);
		}
	});
}

function getSelectedCodeSample(editor) {
	var node = editor.selection.getNode();

	if (isCodeSample(node)) {
		return node;
	}

	return null;
}

function getCurrentCode(editor) {
	var node = getSelectedCodeSample(editor);

	if (node) {
		return node.textContent;
	}

	return '';
}

function getCurrentLanguage(editor) {
	var matches, node = getSelectedCodeSample(editor);

	if (node) {
		matches = node.className.match(/language-(\w+)/);
		return matches ? matches[1] : '';
	}

	return '';
}

function getLineNumbers(editor) {
  var node = getSelectedCodeSample(editor);
  if (node) {
    return checkLineNumbers(node);
  }
  return true;
}

function openDialog(editor) {
	editor.windowManager.open({
		title: "Insert/Edit code sample",
		minWidth: Math.min(DOM.getViewPort().w, editor.getParam('codesample_dialog_width', 800)),
		minHeight: Math.min(DOM.getViewPort().h, editor.getParam('codesample_dialog_height', 650)),
		layout: 'flex',
		direction: 'column',
		align: 'stretch',
		body: [
			{
				type: 'listbox',
				name: 'language',
				label: 'Language',
				maxWidth: 200,
				value: getCurrentLanguage(editor),
				values: getLanguages(editor)
			},
      {
        type: 'checkbox',
        name: 'line_numbers',
        label: 'Show line numbers',
        value: 'true',
        checked: getLineNumbers(editor)
      },
			{
				type: 'textbox',
				name: 'code',
				multiline: true,
				spellcheck: false,
				ariaLabel: 'Code view',
				flex: 1,
				style: 'direction: ltr; text-align: left',
				classes: 'monospace',
				value: getCurrentCode(editor),
				autofocus: true
			}
		],
		onSubmit: function(e) {
			insertCodeSample(editor, e.data.language, e.data.code, e.data.line_numbers);
		}
	});
}

tinymce.PluginManager.add('codesample', function(editor, pluginUrl) {
  var $ = editor.$;

	editor.on('PreProcess', function(e) {
		$('pre[contenteditable=false]', e.node).
			filter(trimArg(isCodeSample)).
			each(function(idx, elm) {
				var $elm = $(elm), code = elm.textContent;
				$elm.attr('class', $.trim($elm.attr('class')));
				$elm.removeAttr('contentEditable');
				$elm.empty().append($('<code></code>').each(function() {
					// Needs to be textContent since innerText produces BR:s
					this.textContent = code;
				}));
			});
	});

	editor.on('SetContent', function() {
    var pre_tags = $('pre');

		var unprocessedCodeSamples = pre_tags.filter(trimArg(isCodeSample)).filter(function(idx, elm) {
			return elm.contentEditable !== "false";
		});

		if (unprocessedCodeSamples.length) {
			editor.undoManager.transact(function() {
				unprocessedCodeSamples.each(function(idx, elm) {
					$(elm).find('br').each(function(idx, elm) {
						elm.parentNode.replaceChild(editor.getDoc().createTextNode('\n'), elm);
					});
					elm.contentEditable = false;
					elm.innerHTML = editor.dom.encode(elm.textContent);
					elm.className = $.trim(elm.className);
				});
			});
		}

    pre_tags.each(function(idx, elm) {
      if (!elm.getElementsByTagName('code').length) {
        wrapCode(elm);
      }
      Prism.highlightElement(elm.firstChild);
    });
	});

	editor.addCommand('codesample', function() {
		openDialog(editor);
	});

	editor.addButton('codesample', {
		cmd: 'codesample',
		title: 'Insert/Edit code sample'
	});

});
