import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://crohfqrvihedoxvksmpc.supabase.co'
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNyb2hmcXJ2aWhlZG94dmtzbXBjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTczNTAxOTAsImV4cCI6MjAzMjkyNjE5MH0.k_-el1npvcpfgdRjOFkpDoZg7rheMbDD03miChH966g'
export const supabase = createClient(supabaseUrl, supabaseKey)
