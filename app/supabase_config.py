from supabase import create_client

# Supabase configuration - project name = " TempoPlan_Flet_Python ", pass = " y2VXdgz4raDPCcio "
supabase_url = "https://zbccvhlvmgsophucuaie.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpiY2N2aGx2bWdzb3BodWN1YWllIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxMjYwODUxNCwiZXhwIjoyMDI4MTg0NTE0fQ.Hn3nLNGn56aOODSBHokJ7bVqtpuLlr2NZ9Tc-J6GiX4"

supabase = create_client(supabase_url, supabase_key)
