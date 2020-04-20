import express from 'express';
import api from '../api';

const BASE = {
  SLASH: '/',
  SLASH_URL: '/:url'
}

const router = express.Router();

router.post(BASE.SLASH, api.addUrl);

export default router;
