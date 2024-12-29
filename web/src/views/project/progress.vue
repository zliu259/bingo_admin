<template>
  <n-space vertical>
    <n-steps size="small" :current=props.status :status='process'>
      <n-step
        title="Quotation"
        description="获取报价"
      />
      <n-step
        title="Payment"
        description="等待付款"
      />
      <n-step
        title="Working"
        description="任务处理"
      />
      <n-step
        title="Review"
        description="结果审查"
      />
      <n-step
        title="Documentation"
        description="生成文档"
      />
      <n-step
        title="Delivery"
        description="交付结果"
      />
    </n-steps>
  </n-space>
</template>

<script lang="ts" setup>
import type { StepsProps } from 'naive-ui'
import { MdArrowRoundBack, MdArrowRoundForward } from '@vicons/ionicons4'
import { ref } from 'vue'

const props = defineProps<{
  status: string
}>()



</script>