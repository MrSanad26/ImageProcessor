# ImageProcessor
## With OpenCV, tkinter and pillow

الكود هو برنامج بسيط عبارة عن معالجة الصور، يتم تنفيذه باستخدام بايثون والمكتبات OpenCV وtkinter  وPIL.

أولا قمت ب استدعاء المكتبات السطر الأول  OpenCV والسطر الثاني tkinter. 

السطر الثالث مكتبة messagebox من tkinter والسطر الرابع مكتبة filedialog من tkinter.
السطر الخامس مكتبة Image و ImageTk من PIL والسطر السادس مكتبة ttk من tkinter.

تم إنشاء فئة ImageProcessor التي تحتوي على الدوال المطلوبة لتشغيل البرنامج.

تم تعريف الدالة init التي تقوم بتهيئة وتكوين نافذة tkinter وإضافة العناصر المختلفة مثل الأزرار والشرائط والإطارات وتحديد نوع المدخلات للبرنامج.

تصميم الشكل وتحديد أماكن الbutton  و slider  وغيرها من المدخلات. 

تم تعريف دالة add_image التي تعرض مربع boutton لاختيار ملف الصورة وإذا تم تحديد الصورة يتم تحميل الصورة في البرنامج من خلال مسار الصورة (path).

تم تعريف دالة show_image التي تقوم بعرض الصورة المحملة في البرنامج.

تم تعريف دالة change_size التي تقوم بتغيير حجم الصورة المحملة من خلال اخذ الطول والعرض في filed وبعدها في زر لاستدعاء الدالة وتغير الحجم وفي حال قام المستخدم بإدخال احرف تظهر رسالة خطاء.

تم تعريف دالة rotate التي تقوم بتدوير الصورة المحملة بزاوية محددة من خلال استدعاء الدالة slider.

تم تعريف دالة blur_image التي تقوم بتطبيق تأثير الضبابية على الصورة المحملة محددة شدة الضباب من خلال استدعاء الدالة slider. 

تم تعريف دالة canny_image التي تقوم بالكشف عن حواف الصورة المحملة ومدى شدة التركيز على الحواف ويتم استدعاء الدالة باستخدام slider.

تم تعريف دالة grayscale التي تقوم بتحويل الصورة المحملة إلى اللون الرمادي ويتم استدعاء الدالة من خلال ضغطت زر.

تم تعريف دالة reset التي تعيد الصورة المحملة إلى حالتها الأصلية وتعيد جميع الإعدادات إلى الوضع الافتراضي ومن ناحية العرض كان الزر صورة إعادة عرض.

تم تعريف دالة save التي تقوم بحفظ الصورة المعالجة في الملفات ويتم استدعاها من خلال الزر الذي على شكل علامة حفظ.

تم تعريف دالة show_result التي تعرض الصورة المعالجة في نافذة جديدة من خلال انشاء نافذة اخرا وعرض النتيجة عليها.

صورة توضيحية لتصميم:

![image](https://github.com/MrSanad26/ImageProcessor/assets/98082864/60fff6e9-835f-42e5-9bd8-7c4a450347d9)


reset button icon
you we find the icon in link first one on the left, color white size 50x50:
https://icons8.com/icons/set/reset

save button icon
you we find the icon in link first one on the left, color white size 50x50:
https://icons8.com/icons/set/save

show ressult button icon
you we find the icon in link first one on the left, color white size 50x50:
https://icons8.com/icons/set/show-result


