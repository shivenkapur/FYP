"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _setupDatabase = _interopRequireDefault(require("../pubSubFunctions/setupDatabase.js"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }

function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }

var client = undefined;
var _default = {
  setClient: function setClient(clientObject) {
    client = clientObject;
  },
  getClient: function () {
    var _getClient = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee() {
      return regeneratorRuntime.wrap(function _callee$(_context) {
        while (1) {
          switch (_context.prev = _context.next) {
            case 0:
              if (!(client == undefined)) {
                _context.next = 3;
                break;
              }

              _context.next = 3;
              return (0, _setupDatabase["default"])();

            case 3:
              return _context.abrupt("return", client);

            case 4:
            case "end":
              return _context.stop();
          }
        }
      }, _callee);
    }));

    function getClient() {
      return _getClient.apply(this, arguments);
    }

    return getClient;
  }()
};
exports["default"] = _default;