<template>
  <n-space vertical>
    <n-steps :current="current as number" :status="currentStatus">
      <n-step
        title="Quotation"
        description="获得报价"
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
        description="审查结果"
      />
      <n-step
        title="Documentation"
        description="制作文档"
      />
      <n-step
        title="Delivering"
        description="交付"
      />
    </n-steps>
    <n-space>
      <n-button-group>
        <n-button @click="prev">
          <template #icon>
            <n-icon>
              <MdArrowRoundBack />
            </n-icon>
          </template>
        </n-button>
        <n-button @click="next">
          <template #icon>
            <n-icon>
              <MdArrowRoundForward />
            </n-icon>
          </template>
        </n-button>
      </n-button-group>
      <n-radio-group v-model:value="currentStatus" size="medium" name="basic">
        <n-radio-button value="error">
          Error
        </n-radio-button>
        <n-radio-button value="process">
          Process
        </n-radio-button>
        <n-radio-button value="wait">
          Wait
        </n-radio-button>
        <n-radio-button value="finish">
          Finish
        </n-radio-button>
      </n-radio-group>
    </n-space>
  </n-space>
</template>

<script lang="ts">
import type { StepsProps } from 'naive-ui'
import { MdArrowRoundBack, MdArrowRoundForward } from '@vicons/ionicons4'
import { defineComponent, ref } from 'vue'

export default defineComponent({
  components: {
    MdArrowRoundBack,
    MdArrowRoundForward
  },
  setup() {
    const currentRef = ref<number | null>(1)
    return {
      currentStatus: ref<StepsProps['status']>('process'),
      current: currentRef,
      next() {
        if (currentRef.value === null)
          currentRef.value = 1
        else if (currentRef.value >= 7)
          currentRef.value = null
        else currentRef.value++
      },
      prev() {
        if (currentRef.value === 0)
          currentRef.value = null
        else if (currentRef.value === null)
          currentRef.value = 7
        else currentRef.value--
      }
    }
  }
})
</script>