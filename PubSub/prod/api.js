"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _publish3 = _interopRequireDefault(require("./pubSubFunctions/publish/publish.js"));

var _subscribe3 = _interopRequireDefault(require("./pubSubFunctions/subscribe/subscribe.js"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }

function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }

var _default = {
  publish: function () {
    var _publish2 = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee(channel, message) {
      var response;
      return regeneratorRuntime.wrap(function _callee$(_context) {
        while (1) {
          switch (_context.prev = _context.next) {
            case 0:
              _context.next = 2;
              return (0, _publish3["default"])(channel, message);

            case 2:
              response = _context.sent;
              return _context.abrupt("return", response);

            case 4:
            case "end":
              return _context.stop();
          }
        }
      }, _callee);
    }));

    function publish(_x, _x2) {
      return _publish2.apply(this, arguments);
    }

    return publish;
  }(),
  subscribe: function () {
    var _subscribe2 = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee2(channel, callback) {
      var response;
      return regeneratorRuntime.wrap(function _callee2$(_context2) {
        while (1) {
          switch (_context2.prev = _context2.next) {
            case 0:
              _context2.next = 2;
              return (0, _subscribe3["default"])(channel, callback);

            case 2:
              response = _context2.sent;
              return _context2.abrupt("return", response);

            case 4:
            case "end":
              return _context2.stop();
          }
        }
      }, _callee2);
    }));

    function subscribe(_x3, _x4) {
      return _subscribe2.apply(this, arguments);
    }

    return subscribe;
  }()
};
exports["default"] = _default;