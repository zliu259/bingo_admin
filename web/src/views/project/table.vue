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
    emit('show-details', rowData.job_id)
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

function createColumns({ showDetails }) {
  return [
    {
      title: 'Active',
      key: 'active',
      render(row) {
        const statusColorMap = {
          True: 'success',
          False: 'warning',
        }
        return h(
          NTag,
          {
            type: statusColorMap[row.active] || 'default',
            bordered: false,
          },
          { default: () => row.active }
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
        const jobTypeMap = {
          1: 'Translation',
          2: 'Interpretation',
          3: 'Certified Copy',
        }
        const jobTypeColorMap = {
          1: 'info',
          2: 'success',
          3: 'warning',
        }
        const jobType = jobTypeMap[row.job_type] || 'Unknown'
        return h(
          NTag,
          {
            type: jobTypeColorMap[row.job_type] || 'default',
            bordered: false,
          },
          { default: () => jobType }
        )
      },
    },
    {
      title: 'Due Date',
      key: 'due_date',
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
  margin: 10px;
}
</style>
