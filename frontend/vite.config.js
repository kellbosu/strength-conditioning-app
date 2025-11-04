import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      'api': 'http://127.0.0.1:8000,' // Whenever frontend makes a request to /api/..., forward it to FastAPI on port 8000..
    }
  }
})

