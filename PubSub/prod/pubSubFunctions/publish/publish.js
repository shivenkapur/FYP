"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = publish;

var _databaseObjects = _interopRequireDefault(require("../../configuration/databaseObjects.js"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }

function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }

function publish(_x, _x2) {
  return _publish.apply(this, arguments);
}

function _publish() {
  _publish = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee(channel, message) {
    var client;
    return regeneratorRuntime.wrap(function _callee$(_context) {
      while (1) {
        switch (_context.prev = _context.next) {
          case 0:
            _context.next = 2;
            return _databaseObjects["default"].getClient();

          case 2:
            client = _context.sent;
            _context.prev = 3;
            _context.next = 6;
            return client.publish(channel, message);

          case 6:
            return _context.abrupt("return", 'Published');

          case 9:
            _context.prev = 9;
            _context.t0 = _context["catch"](3);
            return _context.abrupt("return", 'Something went wrong! Could not publish.');

          case 12:
          case "end":
            return _context.stop();
        }
      }
    }, _callee, null, [[3, 9]]);
  }));
  return _publish.apply(this, arguments);
}