# SDK: TypeScript (sms-typescript)

- **مخزن:** [IPeCompany/SmsPanelV2.TypeScript](https://github.com/IPeCompany/SmsPanelV2.TypeScript)
- **نصب:** `npm install sms-typescript`
- **لایسنس:** MIT
- **پیش‌نیاز:** Node.js ≥ 18 (به دلیل استفاده از `fetch` نیتیو)، TypeScript ≥ 4.5 در صورت استفاده از TS

این پکیج جدیدترین و کامل‌ترین SDK رسمی sms.ir است: تایپ‌های کامل TypeScript، پشتیبانی از CommonJS و ES Modules، دو API طراحی (کلاس‌محور و تابع‌محور)، و سازگاری کامل با نسخه‌ی قبلی (v1.x).

## نصب و راه‌اندازی

### API کلاس‌محور (مناسب برای برنامه‌نویسی شیءگرا)

```ts
import { Smsir } from "sms-typescript";

const sms = new Smsir("your-api-key", lineNumber);
```

### API تابع‌محور (مناسب برای برنامه‌نویسی تابعی)

```ts
import { smsBuilder } from "sms-typescript";

const sms = smsBuilder({
  apiKey: "your-api-key",
  lineNumber: lineNumber,
});
```

> API تابع‌محور شامل متدهای منسوخ‌شده (deprecated) نسخه‌ی v1.x نیست.

### CommonJS (Node.js)

```js
const { Smsir } = require("sms-typescript");
const sms = new Smsir("your-api-key", lineNumber);
```

## مرجع متدها

### `sendBulk(messageText, mobiles, sendDateTime?, customLineNumber?)`

ارسال پیامک گروهی — معادل [3.1. ارسال گروهی](../03-sends/01-bulk.md).

```ts
const result = await sms.sendBulk(
  "سلام دنیا!",
  ["09123456789", "09987654321"],
  Date.now() + 3600000, // اختیاری: زمان‌بندی برای یک ساعت بعد
  lineNumber              // اختیاری: خط دیگری غیر از خط پیش‌فرض
);
console.log("Pack ID:", result.data.packId);
```

### `sendLikeToLike(messageTexts, mobiles, sendDateTime?, customLineNumber?)`

ارسال نظیر به نظیر — معادل [3.2. ارسال نظیر به نظیر](../03-sends/02-like-to-like.md).

```ts
await sms.sendLikeToLike(
  ["سلام علی", "سلام سارا"],
  ["09121111111", "09122222222"]
);
```

### `deleteScheduled(packId)`

حذف یک بسته‌ی ارسال زمان‌بندی‌شده — معادل [3.3. حذف ارسال زمان‌بندی شده](../03-sends/03-delete-scheduled.md).

```ts
await sms.deleteScheduled("pack-id-here");
```

### `sendVerifyCode(mobile, templateId, parameters)`

ارسال پیامک بر اساس قالب از پیش تعریف‌شده — معادل [3.4. ارسال Verify](../03-sends/04-verify.md).

```ts
await sms.sendVerifyCode("09123456789", templateId, [
  { name: "Code", value: "123456" },
]);
```

### `sendByURL(username, mobile, text, customLine?)`

ارسال با متد URL (روش قدیمی‌تر، برای سازگاری با گذشته) — معادل [3.5. ارسال از طریق URL](../03-sends/05-send-via-url.md).

```ts
await sms.sendByURL("username", "09123456789", "سلام دنیا!");
```

### `reportMessage(messageId)`

وضعیت تحویل یک پیامک خاص — معادل [4.1. گزارش پیامک](../04-reports/01-send-reports.md).

```ts
const report = await sms.reportMessage("876240022");
console.log("Delivery State:", report.data.deliveryState);
```

### `reportDailyPack(pageNumber, pageSize)`

آمار مجموعه‌های ارسال روز جاری با صفحه‌بندی — معادل [4.2. گزارش مجموعه ارسال‌های روز](../04-reports/02-live-pack.md).

```ts
const dailyPack = await sms.reportDailyPack(1, 10);
```

### `reportPackById(packId)`

تمام پیامک‌های یک مجموعه‌ی ارسال خاص — معادل [4.3. گزارش مجموعه ارسال](../04-reports/03-send-pack.md).

```ts
const pack = await sms.reportPackById("pack-id");
```

### `reportTodayLive(pageNumber, pageSize)`

پیامک‌های ارسال‌شده‌ی امروز — معادل [4.4. گزارش ارسال‌های روز](../04-reports/04-send-live.md).

```ts
const today = await sms.reportTodayLive(1, 10);
```

### `reportArchive(fromDate, toDate, pageNumber, pageSize)`

پیامک‌های ارسال‌شده‌ی آرشیو شده در یک بازه‌ی زمانی — معادل [4.5. گزارش ارسال‌های آرشیو شده](../04-reports/05-send-archive.md).

```ts
const archived = await sms.reportArchive(
  Date.now() - 86400000, // دیروز
  Date.now(),
  1,
  10
);
```

### `reportLatestReceive(count)`

آخرین پیامک‌های دریافتی — معادل [4.6. گزارش تازه‌ترین پیامک‌های دریافتی](../04-reports/06-receive-latest.md).

```ts
const received = await sms.reportLatestReceive(100);
```

### `reportReceiveLive(pageNumber, pageSize, sortByNewest)`

پیامک‌های دریافتی امروز — معادل [4.7. گزارش پیامک‌های دریافتی روز](../04-reports/07-receive-live.md).

```ts
const live = await sms.reportReceiveLive(1, 10, true);
```

### `reportReceiveArchive(fromDate, toDate, pageNumber, pageSize)`

پیامک‌های دریافتی آرشیو شده — معادل [4.8. گزارش پیامک‌های دریافتی آرشیو شده](../04-reports/08-receive-archive.md).

```ts
const archivedReceived = await sms.reportReceiveArchive(
  Date.now() - 86400000,
  Date.now(),
  1,
  10
);
```

### `getCredit()`

دریافت مقدار اعتبار حساب — معادل [5.1. دریافت مقدار اعتبار فعلی](../05-settings/01-credit.md). طبق آزمایش عملی، مقدار بازگشتی **تعداد پیامک باقی‌مانده** است، نه مبلغ ریالی (به یادداشت بخش ۵.۱ مراجعه کنید).

```ts
const credit = await sms.getCredit();
```

### `getLineNumbers()`

دریافت لیست خطوط فعال حساب — معادل [5.2. دریافت لیست خطوط](../05-settings/02-line.md).

```ts
const lines = await sms.getLineNumbers();
```

## سازگاری با نسخه‌ی v1.x

متدهای قدیمی (PascalCase مانند `SendBulk`, `SendVerifyCode`, ...) هنوز در API کلاس‌محور کار می‌کنند اما **منسوخ (deprecated)** هستند و طبق برنامه‌ی نگهدارنده‌ها در نسخه‌ی v3.0.0 حذف خواهند شد. توصیه می‌شود از متدهای جدید camelCase استفاده کنید.

## مدیریت خطا

```ts
try {
  const result = await sms.sendBulk("سلام", ["09123456789"]);
  console.log("موفق:", result.data);
} catch (error) {
  console.error("خطا:", error.message);
}
```

## پیوندهای بیشتر

- [مثال‌های تکمیلی (Angular، React، Vue.js)](https://github.com/IPeCompany/SmsPanelV2.TypeScript/blob/main/USAGE_EXAMPLES.md)
- [صفحه‌ی Issues برای گزارش باگ یا درخواست ویژگی](https://github.com/IPeCompany/SmsPanelV2.TypeScript/issues)

---

[بازگشت به فهرست SDKها](README.md) · [بازگشت به فهرست مطالب](../README.md)
