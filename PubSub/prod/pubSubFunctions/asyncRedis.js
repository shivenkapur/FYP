"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }

function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }

var _require = require('util'),
    promisify = _require.promisify;

var _default = {
  publish: function () {
    var _publish = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee(client) {
      var getKeysAsync;
      return regeneratorRuntime.wrap(function _callee$(_context) {
        while (1) {
          switch (_context.prev = _context.next) {
            case 0:
              getKeysAsync = promisify(client.publish).bind(client);
              return _context.abrupt("return", getKeysAsync);

            case 2:
            case "end":
              return _context.stop();
          }
        }
      }, _callee);
    }));

    function publish(_x) {
      return _publish.apply(this, arguments);
    }

    return publish;
  }(),
  on: function () {
    var _on = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee2(client) {
      var onAsync;
      return regeneratorRuntime.wrap(function _callee2$(_context2) {
        while (1) {
          switch (_context2.prev = _context2.next) {
            case 0:
              onAsync = promisify(client.on).bind(client);
              return _context2.abrupt("return", onAsync);

            case 2:
            case "end":
              return _context2.stop();
          }
        }
      }, _callee2);
    }));

    function on(_x2) {
      return _on.apply(this, arguments);
    }

    return on;
  }()
};
exports["default"] = _default;