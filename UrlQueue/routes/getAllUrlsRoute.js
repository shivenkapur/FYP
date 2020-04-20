import express from 'express';
import api from '../api';

const BASE = {
  SLASH: '/',
}

const router = express.Router();

router.get(BASE.SLASH, api.getAllUrls);

export default router;
