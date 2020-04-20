import express from 'express';
import api from '../api';

const BASE = {
  SLASH: '/',
}

const router = express.Router();

router.get(BASE.SLASH, api.getAllKeys);

export default router;
