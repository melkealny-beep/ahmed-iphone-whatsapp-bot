# 📝 ورقة الغش - أوامر Git & Railway

## 🎯 الأوامر اللي هتحتاجها كتير

---

## 📦 بداية المشروع (مرة واحدة)

```bash
# انتقل لمجلد المشروع
cd Desktop/ahmed_iphone_bot

# تهيئة Git
git init
git add .
git commit -m "First commit"

# ربط مع GitHub (غيّر username)
git remote add origin https://github.com/username/ahmed-iphone-bot.git
git branch -M main
git push -u origin main
```

---

## 🔄 تحديث الأسعار أو أي تعديل

```bash
# 1. افتح الملف وعدّل ما تريد

# 2. ثم نفذ الأوامر دي:
git add .
git commit -m "Updated prices"
git push origin main

# خلاص! Railway هيحدث تلقائياً ⚡
```

---

## 🔍 أوامر مفيدة

### شوف حالة Git
```bash
git status
```

### شوف التعديلات
```bash
git diff
```

### شوف سجل الـ Commits
```bash
git log --oneline
```

### إلغاء آخر تعديل (قبل Push)
```bash
git reset --soft HEAD~1
```

---

## 🚀 أوامر Railway CLI (اختياري)

### تثبيت Railway CLI
```bash
# Windows (PowerShell)
iwr https://railway.app/install.ps1 | iex

# Mac/Linux
sh -c "$(curl -fsSL https://railway.app/install.sh)"
```

### تسجيل الدخول
```bash
railway login
```

### ربط المشروع
```bash
railway link
```

### مشاهدة Logs
```bash
railway logs
```

### فتح Dashboard
```bash
railway open
```

---

## 🐛 حل المشاكل

### المشكلة: "Permission denied"
```bash
# الحل: تحقق من صلاحيات Git
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### المشكلة: "Remote already exists"
```bash
# الحل: حذف Remote القديم
git remote remove origin
git remote add origin https://github.com/username/repo.git
```

### المشكلة: Git يقول "Nothing to commit"
```bash
# تأكد إنك عدّلت الملف وحفظته
# ثم:
git add -A
git commit -m "Force commit"
```

---

## 📊 سير العمل الكامل

```
1. عدّل الكود محلياً
         ↓
2. git add .
         ↓
3. git commit -m "message"
         ↓
4. git push origin main
         ↓
5. GitHub يستقبل الكود
         ↓
6. Railway يبني ويرفع تلقائياً
         ↓
7. البوت محدّث! ✅
```

---

## 🎨 Commit Messages جيدة

```bash
git commit -m "Updated iPhone 16 prices"
git commit -m "Added new accessory: AirPods Pro 2"
git commit -m "Fixed warranty info message"
git commit -m "Updated store location and phone"
git commit -m "Added new offer for Ramadan"
```

---

## 🔐 حماية البيانات

### لا ترفع أبداً:
❌ ملف `.env`
❌ أرقام التليفونات الحقيقية
❌ Twilio credentials
❌ أي بيانات حساسة

### ملف .gitignore يمنع رفعها تلقائياً ✅

---

## 📱 تحديث Variables في Railway

### من الموقع:
1. Railway Dashboard
2. اختار المشروع
3. Variables
4. Edit أو Add
5. Save

### أو باستخدام CLI:
```bash
railway variables set KEY=value
```

---

## 🎯 Checklist قبل كل Push

✅ عدّلت الملفات المطلوبة؟
✅ اختبرت التعديلات محلياً؟
✅ كتبت Commit message واضحة؟
✅ متأكد إن .env ما اترفعش؟
✅ الأسعار صحيحة؟

---

## 💡 نصائح للسرعة

### اختصار للأوامر الثلاثة
```bash
# بدل ما تكتب 3 أوامر:
git add . && git commit -m "Quick update" && git push
```

### Alias مفيد (اختياري)
```bash
# أضف في ~/.bashrc أو ~/.zshrc
alias gp="git add . && git commit -m 'Quick update' && git push"

# استخدمها:
gp
```

---

## 🔄 النسخ الاحتياطي

### حفظ نسخة محلية
```bash
# من وقت للتاني اعمل:
git clone https://github.com/username/ahmed-iphone-bot.git backup
```

### تحميل من GitHub
```bash
git clone https://github.com/username/ahmed-iphone-bot.git
cd ahmed-iphone-bot
```

---

## 📈 مراقبة التطبيق

### Railway Dashboard:
- **Metrics**: الاستخدام والأداء
- **Logs**: الأخطاء والرسائل
- **Deployments**: سجل النشر
- **Settings**: الإعدادات

### تفعيل الإشعارات:
Railway → Settings → Notifications → Enable

---

## 🆘 الأوامر الطارئة

### إعادة تشغيل سريعة (Railway)
```bash
railway restart
```

### استرجاع آخر نسخة شغالة
```bash
# من Railway Dashboard
Deployments → اختار آخر deploy ناجح → Redeploy
```

### حذف جميع التعديلات المحلية
```bash
git reset --hard HEAD
git clean -fd
```

---

## 📞 أسئلة شائعة

**س: كم مرة أقدر أعمل Push؟**
ج: غير محدود! لكن كل Push = نشر جديد = استهلاك وقت

**س: Railway بياخد وقت قد إيه؟**
ج: عادة 1-3 دقائق

**س: لو نسيت أرفع ملف؟**
ج: عادي، عدّل وارفع تاني

**س: ممكن أشتغل من كذا جهاز؟**
ج: أيوه! استخدم `git pull` قبل ما تشتغل

---

**صُنع بـ ❤️ لأحمد الصعيدي**

احفظ الورقة دي، هتحتاجها! 📌

