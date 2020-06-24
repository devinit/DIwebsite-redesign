var WagtailAceEditor =
/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/visualisation/widgets/ace-editor.ts");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/visualisation/widgets/ace-editor.ts":
/*!*************************************************!*\
  !*** ./src/visualisation/widgets/ace-editor.ts ***!
  \*************************************************/
/*! exports provided: init */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"init\", function() { return initAceEditor; });\n// TODO: find proper types for ace\n// eslint-disable-line @typescript-eslint/no-explicit-any\nvar renderChart = function renderChart(options, element) {\n  element.innerHTML = '';\n\n  var _JSON$parse = JSON.parse(options),\n      data = _JSON$parse.data,\n      layout = _JSON$parse.layout;\n\n  return Plotly.newPlot(element, data, layout);\n};\n\nvar initPlotlyPreview = function initPlotlyPreview(widgetID, options) {\n  var previewNode = document.getElementById(\"\".concat(widgetID, \"-plotly-preview\"));\n\n  if (previewNode) {\n    try {\n      renderChart(options, previewNode);\n      return {\n        onUpdate: function onUpdate(options) {\n          try {\n            renderChart(options, previewNode);\n          } catch (error) {\n            previewNode.innerHTML = \"Rendering Error: \".concat(error.message);\n          }\n        }\n      };\n    } catch (error) {\n      previewNode.innerHTML = \"Rendering Error: \".concat(error.message);\n    }\n  }\n\n  return null;\n};\n\nvar initAceEditor = function initAceEditor(widgetID) {\n  if (widgetID) {\n    var editorNode = document.getElementById(\"\".concat(widgetID, \"-ace-editor\"));\n    var inputNode = document.getElementById(widgetID);\n\n    if (editorNode && inputNode) {\n      try {\n        var editor = ace.edit(editorNode);\n        editor.setTheme('ace/theme/monokai'); //TODO: set theme dynamically\n\n        editor.session.setMode('ace/mode/json'); //TODO: set mode dynamically\n\n        var preview = initPlotlyPreview(widgetID, inputNode.value);\n        editor.getSession().on('change', function () {\n          inputNode.value = editor.getSession().getValue();\n\n          if (preview) {\n            preview.onUpdate(inputNode.value);\n          } else {\n            preview = initPlotlyPreview(widgetID, inputNode.value);\n          }\n        });\n      } catch (error) {\n        editorNode.innerHTML = \"Rendering Error: \".concat(error.message);\n      }\n    }\n  }\n};\n\n\n\n//# sourceURL=webpack://WagtailAceEditor/./src/visualisation/widgets/ace-editor.ts?");

/***/ })

/******/ });