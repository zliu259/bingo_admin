<template>
  <n-spin :show="loading">
    <n-data-table
      :bordered="false"
      :columns="columns"
      :data="data"
      :pagination="pagination"
      class="main-table"
    />
  </n-spin>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { NButton, NTag, useMessage, NSpin } from 'naive-ui'
import api from '@/api'

const emit = defineEmits(['show-details'])

const data = ref([])
const loading = ref(true)
const columns = createColumns({
  sendMail(rowData) {
    message.info(`send mail to ${rowData.name}`)
  },
  showDetails(rowData) {
    emit('show-details', rowData.uuid)
  },
})
const pagination = {
  pageSize: 10,
}

onMounted(async () => {
  try {
    const response = await api.getProjectList()
    data.value = response.data
  } catch (error) {
    console.error('Failed to fetch project list:', error)
  } finally {
    loading.value = false
  }
})

function createColumns({ sendMail, showDetails }) {
  return [
    {
      title: 'Status',
      key: 'status',
      render(row) {
        const statusColorMap = {
          Pending: 'warning',
          Completed: 'success',
          'In Progress': 'info',
        }
        return h(
          NTag,
          {
            type: statusColorMap[row.status] || 'default',
            bordered: false,
          },
          { default: () => row.status }
        )
      },
    },
    {
      title: 'Job ID',
      key: 'job_id',
    },
    {
      title: 'Date',
      key: 'date',
    },
    {
      title: 'Client Name',
      key: 'client',
    },
    {
      title: 'Job Type',
      key: 'job_type',
      render(row) {
        const jobTypeColorMap = {
          'Type 1': 'info',
          'Type 2': 'success',
          'Type 3': 'warning',
        }
        return h(
          NTag,
          {
            type: jobTypeColorMap[row.jobType] || 'default',
            bordered: false,
          },
          { default: () => row.jobType }
        )
      },
    },
    {
      title: 'Due Date',
      key: 'due',
    },
    {
      title: 'Action',
      key: 'actions',
      render(row) {
        return h('div', [
          h(
            NButton,
            {
              strong: true,
              secondary: true,
              size: 'small',
              type: 'success',
              onClick: () => showDetails(row),
            },
            { default: () => 'Details' }
          ),
          h(
            NButton,
            {
              strong: true,
              secondary: true,
              size: 'small',
              style: { marginLeft: '10px' },
              type: 'error',
              onClick: () => console.log('terminated'),
            },
            { default: () => 'Terminate' }
          ),
        ])
      },
    },
  ]
}

const message = useMessage()
</script>

<style scoped>
.main-table {
  height: 50%;
  margin: 20px;
}
</style>