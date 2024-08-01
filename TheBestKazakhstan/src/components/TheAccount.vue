<template>
    <div>
        <h1>User Details</h1>
        <div v-if="user">
          <p><strong>First Name:</strong> {{ user.firstname }}</p>
          <p><strong>Last Name:</strong> {{ user.lastname }}</p>
          <p><strong>Login:</strong> {{ user.login }}</p>
          <p><strong>Phone Number:</strong> {{ user.phonenumber }}</p>
          <p><strong>Created At:</strong> {{ new Date(user.created_at).toLocaleString() }}</p>
        </div>
        <div v-else>
          <p>Loading...</p>
        </div>
      </div>
</template>

<script>
import { supabase } from './SupabaseClient.js'

export default {
    data() {
        return {
            user: null
        }
    },
    async mounted() {
    const { data, error } = await supabase
      .from('users') // замените на правильное имя таблицы
      .select('*')
      .eq('id', '9bef0eeb-a27d-4d0d-9828-9200be823f7b') 
      .single()

    if (error) {
      console.error('Error fetching user:', error)
    } else {
      this.user = data
    }
  },
}
</script>