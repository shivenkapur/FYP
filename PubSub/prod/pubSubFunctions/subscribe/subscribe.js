"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = subscribe;

function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }

function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }

var redis = require("redis");

function subscribe(_x, _x2) {
  return _subscribe.apply(this, arguments);
}

function _subscribe() {
  _subscribe = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee(channel, callback) {
    var subscriber;
    return regeneratorRuntime.wrap(function _callee$(_context) {
      while (1) {
        switch (_context.prev = _context.next) {
          case 0:
            subscriber = redis.createClient();
            subscriber.on("message", callback);
            subscriber.subscribe(channel);

          case 3:
          case "end":
            return _context.stop();
        }
      }
    }, _callee);
  }));
  return _subscribe.apply(this, arguments);
}