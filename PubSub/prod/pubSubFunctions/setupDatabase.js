"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = setupDatabase;

var _databaseObjects = _interopRequireDefault(require("../configuration/databaseObjects.js"));

var _asyncRedis = _interopRequireDefault(require("./asyncRedis.js"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }

function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }

var redis = require("redis");

function setupDatabase() {
  return _setupDatabase.apply(this, arguments);
}

function _setupDatabase() {
  _setupDatabase = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee() {
    var client, asyncOn, connectStatus;
    return regeneratorRuntime.wrap(function _callee$(_context) {
      while (1) {
        switch (_context.prev = _context.next) {
          case 0:
            _context.next = 2;
            return redis.createClient();

          case 2:
            client = _context.sent;
            _context.next = 5;
            return _asyncRedis["default"].on(client);

          case 5:
            asyncOn = _context.sent;
            _context.next = 8;
            return asyncOn('connect');

          case 8:
            connectStatus = _context.sent;
            console.log("Connected: ", connectStatus);
            /*connectStatus = await asyncOn('error');
            console.log("Error: ", connectStatus);*/

            _databaseObjects["default"].setClient(client);

          case 11:
          case "end":
            return _context.stop();
        }
      }
    }, _callee);
  }));
  return _setupDatabase.apply(this, arguments);
}