import express from 'express';
import api from '../api';

const BASE = {
  SLASH: '/'
}

const router = express.Router();

router.post(BASE.SLASH, api.createNode);

export default router;
