<script setup>
import { ref, onMounted } from 'vue'
import { useMessage, useDialog } from 'naive-ui'
import { v7 as uuidv7 } from 'uuid'
import api from '@/api'

const formRef = ref(null)
const message = useMessage()
const dialog = useDialog()

const model = ref({
  job_id: '',
  date: null,
  job_type: null,
  due_date: null,
  client: '',
  client_contact: '',
  contact_method: [],
  contact_details: '',
  created_by: '',
  created_time: null,
})

const clientOptions = ref([])

onMounted(async () => {
  model.value.job_id = uuidv7()
  const user = await api.getUserInfo()
  console.log(user.data.username)
  model.value.created_by = user.data.username // Assuming the user object has a username property
  model.value.created_time = new Date() // Set created_time to current time

  // Fetch client options
  const clients = await api.getClients() // Assuming this API call exists
  clientOptions.value = clients.data.map(client => ({
    label: client.name,
    value: client.id
  }))
})

const jobTypeOptions = [
  { label: 'Translation', value: 1 },
  { label: 'Interpretation', value: 2 },
  { label: 'Certified Copy', value: 3 },
]

const contactMethodOptions = [
  { label: 'Email', value: 'Email' },
  { label: 'WeChat', value: 'WeChat' },
  { label: 'Phone', value: 'Phone' },
  { label: 'Post', value: 'Post' },
  { label: 'Others', value: 'Others' },
]

const handleSubmit = () => {
  dialog.info({
    title: 'Confirm Submission',
    content: `Please confirm the following details:\n\n${JSON.stringify(model.value, null, 2)}`,
    positiveText: 'Confirm',
    negativeText: 'Cancel',
    onPositiveClick: () => {
      message.success('Form submitted successfully')
    },
    onNegativeClick: () => {
      message.info('Submission cancelled')
    }
  })
}
</script>

<template>
  <div class="form">
    <n-form ref="formRef" :model="model" label-placement="top">
      <n-grid :cols="24" :x-gap="24">
        <!-- Basic Info -->
        <n-form-item-gi :span="12" label="Job ID" path="job_id">
          <n-input v-model:value="model.job_id" placeholder="Job ID" readonly />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Date" path="date">
          <n-date-picker v-model:value="model.date" type="datetime" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Job Type" path="job_type">
          <n-select
            v-model:value="model.job_type"
            :options="jobTypeOptions"
            placeholder="Job Type"
          />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Due Date" path="due_date">
          <n-date-picker v-model:value="model.due_date" type="datetime" />
        </n-form-item-gi>

        <!-- Client Info -->
        <n-form-item-gi :span="12" label="Client" path="client">
          <n-select
            v-model:value="model.client"
            :options="clientOptions"
            placeholder="Select Client"
          />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Client Contact" path="client_contact">
          <n-input v-model:value="model.client_contact" placeholder="Client Contact" />
        </n-form-item-gi>

        <!-- Contact Info -->
        <n-form-item-gi :span="12" label="Contact Method" path="contact_method">
          <n-select
            v-model:value="model.contact_method"
            :options="contactMethodOptions"
            placeholder="Select Contact Method"
            multiple
          />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Contact Details" path="contact_details">
          <n-input v-model:value="model.contact_details" placeholder="Contact Details" />
        </n-form-item-gi>

        <!-- System Info -->
        <n-form-item-gi :span="12" label="Created By" path="created_by">
          <n-input v-model:value="model.created_by" placeholder="Created By" readonly />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Created Time" path="created_time">
          <n-date-picker v-model:value="model.created_time" type="datetime" />
        </n-form-item-gi>

        <n-gi :span="24">
          <div style="display: flex; justify-content: flex-end">
            <n-button round type="primary" @click="handleSubmit">Submit</n-button>
          </div>
        </n-gi>
      </n-grid>
    </n-form>
    <pre>{{ JSON.stringify(model, null, 2) }}</pre>
  </div>
</template>