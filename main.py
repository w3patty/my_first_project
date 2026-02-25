import random

import streamlit as st
import time

# ----------------- НАСТРОЙКА СТРАНИЦЫ -----------------
st.set_page_config(page_title="EduPlatform 2026", layout="wide", page_icon="🎓")

# ----------------- SOFT TECH СТИЛИЗАЦИЯ (LIGHT MODE) -----------------
st.markdown("""
<style>
    /* 1. Общий фон: Чистый, светлый, с легким градиентом */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');

    .stApp { 
        background: radial-gradient(at 0% 0%, #f8fafc 0, transparent 50%), 
                    radial-gradient(at 100% 100%, #eff6ff 0, transparent 50%);
        background-color: #ffffff;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* 2. Навигация: Сетчатый «стеклянный» эффект */
    div[data-testid="stHorizontalBlock"] {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        padding: 8px 15px;
        border-radius: 18px;
        border: 1px solid rgba(226, 232, 240, 0.8);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
        margin-bottom: 30px;
    }

    div[data-testid="stHorizontalBlock"] button {
        color: #64748b !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        border: none !important;
        background: transparent !important;
        transition: all 0.3s ease;
    }

    div[data-testid="stHorizontalBlock"] button:hover {
        color: #2563eb !important;
        transform: translateY(-1px);
    }

    /* 3. Заголовки и акценты: Насыщенный синий */
    h1, h2, h3, b, strong {
        color: #1e293b !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em;
    }

    /* Синие «умные» акценты */
    .blue-highlight { color: #2563eb; }

    /* 4. Карточки: Объемные и мягкие */
    .news-card, .job-card, .lib-card-container, .pricing-card {
        background: #ffffff !important;
        border: 1px solid #f1f5f9 !important;
        border-radius: 24px !important;
        padding: 24px !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.02), 0 4px 6px -4px rgba(0, 0, 0, 0.02);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .job-card:hover, .pricing-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 20px 25px -5px rgba(37, 99, 235, 0.1), 0 8px 10px -6px rgba(37, 99, 235, 0.05) !important;
        border-color: #dbeafe !important;
    }

    /* 5. Детализация: Декоративные элементы */
    .news-card::before {
        content: "";
        display: block;
        width: 40px;
        height: 4px;
        background: #2563eb;
        border-radius: 10px;
        margin-bottom: 12px;
    }

    /* 6. Кнопки: Современный плоский стиль */
    .stButton>button {
        background: #1e293b !important;
        color: #ffffff !important;
        border-radius: 14px !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        border: 1px solid #1e293b !important;
        box-shadow: 0 4px 12px rgba(30, 41, 59, 0.15) !important;
    }

    .stButton>button:hover {
        background: #2563eb !important;
        border-color: #2563eb !important;
        transform: translateY(-2px);
    }

    /* 7. Метрики: Чистые и крупные */
    [data-testid="stMetric"] {
        background: white;
        padding: 15px;
        border-radius: 20px;
        border: 1px solid #f1f5f9;
    }

    /* 8. ИИ-Ассистент: Плавающий виджет */
    .ai-box {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        color: #1e293b !important;
        border-radius: 28px !important;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15) !important;
    }
</style>
""", unsafe_allow_html=True)
# ----------------- СОСТОЯНИЕ -----------------
if 'auth' not in st.session_state: st.session_state.auth = False
if 'active_tab' not in st.session_state: st.session_state.active_tab = "Главная"
if 'test_step' not in st.session_state: st.session_state.test_step = 0
if 'answers' not in st.session_state: st.session_state.answers = {}

# ----------------- ИСПРАВЛЕННАЯ РЕГИСТРАЦИЯ (КЛАССЫ ВЕРНУЛИСЬ) -----------------
if not st.session_state.auth:
    _, col_main, _ = st.columns([1, 2, 1])

    with col_main:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 30px; animation: fadeInUp 0.8s ease-out;">
                <h1 style="font-size: 40px;">🚀 EduPlatform 2026</h1>
                <p style="font-size: 16px; opacity: 0.8;">Твой путь в IT начинается здесь</p>
            </div>
        """, unsafe_allow_html=True)

        with st.container():
            st.markdown('<div class="pricing-card" style="text-align: left; padding: 40px;">', unsafe_allow_html=True)

            st.subheader("📝 Создай свой профиль")

            # Аватар
            st.write("Выбери свой аватар:")
            avatar_list = ["🚀", "💻", "🧠", "🕶️", "⚡", "🤖", "🎨", "🛡️"]
            selected_avatar = st.select_slider("Аватар", options=avatar_list, value="🚀", label_visibility="collapsed")

            # Поля
            u_name = st.text_input("Как тебя зовут?", placeholder="Например, Иван")
            u_email = st.text_input("Твой Email", placeholder="example@mail.com")

            # Возвращаем выбор классов
            st.write("В каком ты классе?")
            u_status = st.radio(
                "Класс",
                ["9 класс", "10 класс", "11 класс", "Взрослый"],
                horizontal=True,
                label_visibility="collapsed"
            )

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button("Начать обучение ✨", use_container_width=True):
                if not u_name or not u_email:
                    st.error("Пожалуйста, введи имя и email!")
                elif "@" not in u_email:
                    st.warning("Проверь корректность email (нужна @)!")
                else:
                    with st.spinner("Создаем твою цифровую личность..."):
                        time.sleep(1)
                        st.session_state.auth = True
                        st.session_state.user_name = u_name
                        st.session_state.user_avatar = selected_avatar
                        st.session_state.user_level = u_status  # Теперь здесь будет "9 класс", "10 класс" и т.д.
                        st.balloons()
                        st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

    st.stop()
# ----------------- ВЕРХНЯЯ НАВИГАЦИЯ -----------------
tabs = ["Главная", "Опросник", "Профессии", "Библиотека", "Мини-игра", "Подписка"]
nav_cols = st.columns(len(tabs))
for i, tab_name in enumerate(tabs):
    with nav_cols[i]:
        if st.button(tab_name, use_container_width=True, key=f"nav_{tab_name}"):
            st.session_state.active_tab = tab_name
            st.rerun()

st.markdown("<hr style='margin: 0px 0 25px 0; opacity: 0.1;'>", unsafe_allow_html=True)

# --- 1. ГЛАВНАЯ (ХАБ) ---
if st.session_state.active_tab == "Главная":
    st.markdown(
        f"<div style='text-align: center; padding-bottom: 20px;'><h1>EduPlatform 2026 🚀</h1><p>Привет, {st.session_state.user_name}!</p></div>",
        unsafe_allow_html=True)
    c_nav, c_news = st.columns([2, 1])
    with c_nav:
        st.subheader("📍 Навигация")
        n1, n2 = st.columns(2)
        if n1.button("🧠 Тесты", use_container_width=True): st.session_state.active_tab = "Опросник"; st.rerun()
        if n1.button("💼 Профессии", use_container_width=True): st.session_state.active_tab = "Профессии"; st.rerun()
        if n2.button("📚 Библиотека", use_container_width=True): st.session_state.active_tab = "Библиотека"; st.rerun()
        if n2.button("🎮 Мини-игра", use_container_width=True): st.session_state.active_tab = "Мини-игра"; st.rerun()
    with c_news:
        st.subheader("📢 Новости")
        st.markdown('<div class="news-card"><small>Сегодня</small><br>Gemini 2.0 интегрирован!</div>',
                    unsafe_allow_html=True)
    st.divider()
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Онлайн", "1,240");
    s2.metric("Курсов", "45");
    s3.metric("Баллы", "2,850");
    s4.metric("Ударка", "14 дн")

# --- 2. ОПРОСНИК (УЛУЧШЕННЫЙ ИНТЕРАКТИВНЫЙ ТЕСТ) ---
elif st.session_state.active_tab == "Опросник":
    st.header("🧠 Профориентационный Квест")

    # База вопросов с весами для профессий
    if 'quest_pool' not in st.session_state:
        st.session_state.quest_pool = [
            {
                "q": "Что тебе ближе в творчестве?",
                "opts": {
                    "Логика и алгоритмы": "backend",
                    "Визуал и эстетика": "design",
                    "Поиск скрытых ошибок": "qa"
                }
            },
            {
                "q": "Если бы ты строил дом, ты бы...",
                "opts": {
                    "Рисовал фасад": "design",
                    "Прокладывал сложные коммуникации": "backend",
                    "Проверял стены на прочность": "qa"
                }
            },
            {
                "q": "Какая суперсила тебе нужнее?",
                "opts": {
                    "Предсказывать будущее по данным": "data",
                    "Создавать миры из кода": "frontend",
                    "Защищать от темных сил (хакеров)": "security"
                }
            }
        ]
        st.session_state.test_step = 0
        st.session_state.score = {"backend": 0, "design": 0, "qa": 0, "data": 0, "frontend": 0, "security": 0}

    # Прогресс-бар
    progress = st.session_state.test_step / len(st.session_state.quest_pool)
    st.progress(progress)
    st.write(f"Вопрос {st.session_state.test_step + 1} из {len(st.session_state.quest_pool)}")

    if st.session_state.test_step < len(st.session_state.quest_pool):
        current_q = st.session_state.quest_pool[st.session_state.test_step]

        # Красивая карточка вопроса
        st.markdown(f"""
            <div class="job-card" style="margin-bottom: 20px; border-left: 5px solid #3b82f6;">
                <h2 style="margin: 0;">{current_q['q']}</h2>
            </div>
        """, unsafe_allow_html=True)

        # Выбор ответа кнопками вместо радио
        for text, category in current_q['opts'].items():
            if st.button(text, use_container_width=True, key=f"btn_{text}"):
                st.session_state.score[category] += 1
                st.session_state.test_step += 1
                st.rerun()
    else:
        # Финал: Определение результата
        st.balloons()
        top_category = max(st.session_state.score, key=st.session_state.score.get)

        results = {
            "backend": "Твой путь — Backend Разработчик ⚙️",
            "design": "Ты рожден быть UI/UX Дизайнером ✨",
            "qa": "Твое призвание — QA Инженер (Тестировщик) 🔍",
            "data": "Ты будущий Data Scientist 📊",
            "frontend": "Твой выбор — Frontend Разработчик 🎨",
            "security": "Ты — будущий Кибер-ниндзя (Security Expert) 🛡️"
        }

        st.markdown(f"""
            <div class="pricing-card" style="background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%); color: white; border: none;">
                <h1 style="color: white !important;">Результат теста:</h1>
                <h2 style="color: white !important;">{results[top_category]}</h2>
                <p style="color: rgba(255,255,255,0.8);">На основе твоих ответов мы подобрали идеальное направление в ИТ.</p>
            </div>
        """, unsafe_allow_html=True)

        if st.button("К списку профессий", use_container_width=True):
            st.session_state.active_tab = "Профессии"
            st.rerun()

        if st.button("Пройти заново", type="secondary"):
            del st.session_state.quest_pool
            st.session_state.test_step = 0
            st.rerun()

# ----------------- 3. ПРОФЕССИИ (15 НАПРАВЛЕНИЙ) -----------------
elif st.session_state.active_tab == "Профессии":
    st.header("💼 Навигатор профессий 2026")
    st.subheader("Исследуй востребованные направления и начни свой путь")

    # База данных 15 профессий
    professions_data = [
        {"name": "Frontend Developer", "icon": "🎨", "salary": "450k+", "level": "Средний",
         "skills": ["React/Vue", "TypeScript", "Tailwind CSS"],
         "desc": "Создание интерфейсов, с которыми взаимодействует пользователь."},
        {"name": "Data Scientist", "icon": "📊", "salary": "600k+", "level": "Высокий",
         "skills": ["Python", "Machine Learning", "Statistics"],
         "desc": "Анализ больших данных и построение прогнозных моделей."},
        {"name": "Cybersecurity Expert", "icon": "🛡️", "salary": "550k+", "level": "Высокий",
         "skills": ["Pentesting", "Network Security", "Linux"],
         "desc": "Защита информационных систем от взломов и атак."},
        {"name": "AI Prompt Engineer", "icon": "🤖", "salary": "400k+", "level": "Низкий",
         "skills": ["NLP", "Logic", "Creative Writing"],
         "desc": "Оптимизация запросов для нейросетей типа GPT и Claude."},
        {"name": "DevOps Engineer", "icon": "♾️", "salary": "650k+", "level": "Высокий",
         "skills": ["Docker/K8s", "CI/CD", "AWS/Azure"],
         "desc": "Автоматизация процессов разработки и эксплуатации ПО."},
        {"name": "UI/UX Designer", "icon": "✨", "salary": "350k+", "level": "Средний",
         "skills": ["Figma", "User Flow", "Prototyping"],
         "desc": "Проектирование удобного и красивого пользовательского опыта."},
        {"name": "Backend Developer", "icon": "⚙️", "salary": "500k+", "level": "Средний",
         "skills": ["Python/Go/Node", "PostgreSQL", "API"], "desc": "Разработка серверной логики и баз данных."},
        {"name": "Mobile Dev (Swift/Kotlin)", "icon": "📱", "salary": "480k+", "level": "Средний",
         "skills": ["SwiftUI", "Android SDK", "Architecture"], "desc": "Создание приложений для iOS и Android."},
        {"name": "Blockchain Developer", "icon": "⛓️", "salary": "800k+", "level": "Очень высокий",
         "skills": ["Solidity", "Cryptography", "Smart Contracts"],
         "desc": "Разработка децентрализованных систем и сервисов."},
        {"name": "Game Developer", "icon": "🎮", "salary": "420k+", "level": "Средний",
         "skills": ["C#", "Unity/Unreal Engine", "Math"], "desc": "Создание игровых миров и механик."},
        {"name": "QA Automation", "icon": "🔍", "salary": "380k+", "level": "Низкий",
         "skills": ["Selenium", "Pytest", "Bug Tracking"],
         "desc": "Автоматизированное тестирование качества программ."},
        {"name": "Digital Marketer", "icon": "📈", "salary": "300k+", "level": "Низкий",
         "skills": ["SEO", "Targeting", "Analytics"], "desc": "Продвижение продуктов в цифровой среде."},
        {"name": "VR/AR Architect", "icon": "👓", "salary": "550k+", "level": "Высокий",
         "skills": ["3D Modeling", "C++", "Spatial UX"],
         "desc": "Проектирование миров дополненной и виртуальной реальности."},
        {"name": "Project Manager", "icon": "📅", "salary": "400k+", "level": "Средний",
         "skills": ["Agile/Scrum", "Soft Skills", "Risk Mgmt"],
         "desc": "Управление командой и сроками реализации проектов."},
        {"name": "Fullstack Engineer", "icon": "🌐", "salary": "600k+", "level": "Высокий",
         "skills": ["React", "Node.js", "System Design"], "desc": "Универсальный боец, создающий продукт целиком."}
    ]

    # Рендеринг сеткой 3x5
    cols = st.columns(3)
    for i, prof in enumerate(professions_data):
        with cols[i % 3]:
            # Сама карточка
            st.markdown(f"""
                <div style="background: white; padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                    <div style="font-size: 40px; margin-bottom: 10px;">{prof['icon']}</div>
                    <h3 style="color: #1e3a8a; margin-bottom: 5px;">{prof['name']}</h3>
                    <p style="color: #28a745; font-weight: bold; margin-bottom: 5px;">ЗП: {prof['salary']}</p>
                    <hr style="margin: 10px 0; opacity: 0.2;">
                </div>
            """, unsafe_allow_html=True)

            # Дополнительная информация в выпадающем блоке
            with st.expander("ℹ️ Подробнее"):
                st.write(f"**Описание:** {prof['desc']}")
                st.write(f"**Сложность входа:** {prof['level']}")
                st.write("**Ключевые стеки:**")
                st.code(", ".join(prof['skills']))
                if st.button(f"Выбрать {prof['name']}", key=f"prof_btn_{i}"):
                    st.session_state.user_goal = prof['name']
                    st.toast(f"Цель установлена: {prof['name']}!")

# ----------------- 4. БИБЛИОТЕКА (10 КНИГ С ОБЛОЖКАМИ + 5 КУРСОВ) -----------------
elif st.session_state.active_tab == "Библиотека":
    st.header("📚 Образовательный центр")
    st.subheader("Топ-10 книг 2026 года и связанные с ними курсы")

    # База данных: 10 книг с рабочими ссылками на обложки
    library_data = [
        {
            "title": "Чистый код", "author": "Роберт Мартин", "tag": "Разработка",
            "img": "https://m.media-amazon.com/images/I/41xShlnTZTL._SX376_BO1,204,203,200_.jpg",
            "desc": "Библия для тех, кто хочет писать поддерживаемый и красивый код.",
            "courses": ["Основы Java", "Архитектура ПО", "Рефакторинг", "Unit-тесты", "Clean Code Pro"]
        },
        {
            "title": "Грокаем алгоритмы", "author": "Адитья Бхаргава", "tag": "Computer Science",
            "img": "https://m.media-amazon.com/images/I/91cw36IKp6L.jpg",
            "desc": "Самое простое и наглядное введение в мир алгоритмов и структур данных.",
            "courses": ["Алгоритмы", "Python для профи", "Data Structures", "LeetCode", "Olymp Prog"]
        },
        {
            "title": "Дизайн привычных вещей", "author": "Дон Норман", "tag": "Дизайн / UX",
            "img": "https://m.media-amazon.com/images/I/410vJpYvA6L._SX322_BO1,204,203,200_.jpg",
            "desc": "Как создавать вещи, которыми людям будет удобно пользоваться.",
            "courses": ["UX UI Design", "User Research", "Figma Expert", "Psychology", "Product Design"]
        },
        {
            "title": "Атомные привычки", "author": "Джеймс Клир", "tag": "Продуктивность",
            "img": "https://m.media-amazon.com/images/I/51-nXsSRfZL._SX328_BO1,204,203,200_.jpg",
            "desc": "Как маленькие изменения приводят к огромным результатам.",
            "courses": ["Time Management", "Efficiency", "Neurobiology", "Success Psych", "Biohacking"]
        },
        {
            "title": "Думай медленно... решай быстро", "author": "Даниэль Канеман", "tag": "Психология",
            "img": "https://m.media-amazon.com/images/I/41shS294S5L._SX330_BO1,204,203,200_.jpg",
            "desc": "Шедевр о том, как работает наше мышление и почему мы ошибаемся.",
            "courses": ["Critical Thinking", "Cognitive Psych", "Behavioral Econ", "Decision Making", "Logic"]
        },
        {
            "title": "Не заставляйте меня думать", "author": "Стив Круг", "tag": "Веб-дизайн",
            "img": "https://m.media-amazon.com/images/I/41ovv6p3S9L._SX385_BO1,204,203,200_.jpg",
            "desc": "Ключевые принципы юзабилити веб-интерфейсов.",
            "courses": ["Web Analytics", "HTML & CSS", "Usability Test", "Frontend Dev", "Mobile UX"]
        },
        {
            "title": "Scrum", "author": "Джефф Сазерленд", "tag": "Менеджмент",
            "img": "https://m.media-amazon.com/images/I/51H-pYk663L._SX326_BO1,204,203,200_.jpg",
            "desc": "Метод управления проектами, который изменил мир современной разработки.",
            "courses": ["Agile Project", "Scrum Master", "IT Management", "Kanban", "JIRA Mastery"]
        },
        {
            "title": "Антихрупкость", "author": "Нассим Талеб", "tag": "Бизнес",
            "img": "https://m.media-amazon.com/images/I/416T0S-mGTL._SX323_BO1,204,203,200_.jpg",
            "desc": "Как извлекать выгоду из хаоса и неопределенности в бизнесе и жизни.",
            "courses": ["Risk Management", "Strategy", "Crisis Mgmt", "Investments", "Finance"]
        },
        {
            "title": "Код", "author": "Чарльз Петцольд", "tag": "Computer Science",
            "img": "https://m.media-amazon.com/images/I/41-A8N8M0FL._SX382_BO1,204,203,200_.jpg",
            "desc": "Увлекательное объяснение того, как работают компьютеры на низком уровне.",
            "courses": ["CS Basics", "Hardware", "Low-level Prog", "OS Systems", "Assembler"]
        },
        {
            "title": "Пиши, сокращай", "author": "Максим Ильяхов", "tag": "Копирайтинг",
            "img": "https://m.media-amazon.com/images/I/61S08H5vGvL.jpg",
            "desc": "Как создавать сильные тексты без мусора, фальши и лишних слов.",
            "courses": ["Copywriting", "Storytelling", "Editing", "Content Mark", "SMM Strategy"]
        }
    ]

    for item in library_data:
        with st.container():
            # Карточка книги
            st.markdown(f"""
                <div style="background: white; padding: 25px; border-radius: 15px; border: 1px solid #e0e0e0; margin-bottom: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
                    <div style="display: flex; gap: 25px; flex-wrap: wrap; align-items: flex-start;">
                        <img src="{item['img']}" style="width: 130px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.15); object-fit: contain;">
                        <div style="flex: 1; min-width: 300px;">
                            <span style="background: #e1f5fe; color: #007bff; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold;">{item['tag']}</span>
                            <h2 style="margin: 15px 0 5px 0; color: #1e3a8a; font-size: 24px;">{item['title']}</h2>
                            <p style="margin: 0; color: #64748b; font-size: 16px;"><b>Автор:</b> {item['author']}</p>
                            <p style="margin: 15px 0; font-size: 15px; color: #333; line-height: 1.5;">{item['desc']}</p>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # Кнопки курсов
            st.write(f"**🎓 Курсы к книге «{item['title']}»:**")
            c_cols = st.columns(5)
            for idx, course in enumerate(item['courses']):
                with c_cols[idx]:
                    if st.button(course, key=f"lib_btn_{item['title']}_{idx}", use_container_width=True):
                        st.toast(f"Вы записаны на: {course}")
                        st.success("Успешно!")
            st.markdown("<br>", unsafe_allow_html=True)
# ----------------- 5. МИНИ-ИГРА -----------------
elif st.session_state.active_tab == "Мини-игра":
    st.header("🎮 Симулятор: 10 критических ситуаций")
    st.subheader("Выбери профессию и спаси ситуацию!")

    game_scenarios = {
        "🚀 Пилот": {"issue": "Отказ левого двигателя на высоте 10 000 метров!",
                    "variants": ["Флюгировать винт", "Перезапуск", "Планирование", "SOS", "Балансировка",
                                 "Резкое снижение"]},
        "👨‍⚕️ Хирург": {"issue": "Внезапное падение давления у пациента во время операции!",
                        "variants": ["Адреналин", "Зажим артерии", "Массаж сердца", "Переливание", "Дефибриллятор",
                                     "Кислород"]},
        "💻 Программист": {"issue": "База данных удалена за 5 минут до релиза!",
                          "variants": ["Бэкап", "Git Revert", "Паника", "Логи сервера", "SQL Recovery", "Уволиться"]},
        "🚒 Пожарный": {"issue": "Обратная тяга! Вы заблокированы в горящем помещении!",
                       "variants": ["Вскрыть окно", "Низкий уровень", "Связь с базой", "Поиск выхода", "Стена воды",
                                    "Кислородная маска"]},
        "☢️ Инженер АЭС": {"issue": "Температура в активной зоне реактора критическая!",
                           "variants": ["Графитовые стержни", "Борная кислота", "Охлаждение", "Сброс давления",
                                        "Эвакуация", "Бетонный саркофаг"]},
        "👮 Коп": {"issue": "Погоня на высокой скорости в жилом квартале!",
                  "variants": ["Пит-маневр", "Шипы", "Вертолет", "Перекрытие", "Мегафон", "Ожидание"]},
        "👨‍🏫 Учитель": {"issue": "Весь класс начал спонтанную драку во время теста!",
                        "variants": ["Свисток", "Директор", "Развести углы", "Журнал", "Родители", "Игнорировать"]},
        "🌱 Эколог": {"issue": "Разлив нефти угрожает заповеднику с котиками!",
                     "variants": ["Бонные заграждения", "Сорбенты", "Биоразложение", "Откачка", "Волонтеры",
                                  "Штраф заводу"]},
        "🏗️ Строитель": {"issue": "Подъемный кран начал крениться над дорогой!",
                         "variants": ["Противовес", "Остановка", "Оцепление", "Контргруз", "Прыжок", "Тормоз"]},
        "🧪 Химик": {"issue": "В колбе началась неконтролируемая экзотермическая реакция!",
                    "variants": ["Ледяная баня", "Нейтрализатор", "Вытяжка", "Песок", "Защитный экран", "Огнетушитель"]}
    }

    job_choice = st.selectbox("Кем ты хочешь быть сегодня?", list(game_scenarios.keys()))
    current = game_scenarios[job_choice]
    st.error(f"🚨 *СИТУАЦИЯ:* {current['issue']}")

    col_a, col_b = st.columns(2)
    for i, variant in enumerate(current['variants']):
        target_col = col_a if i % 2 == 0 else col_b
        with target_col:
            if st.button(variant, key=f"ans_{job_choice}_{i}", use_container_width=True):
                with st.spinner('ИИ анализирует последствия...'):
                    time.sleep(1)
                    if i < 3:
                        st.balloons()
                        st.success(f"✅ Великолепно! Действие '{variant}' спасло ситуацию. Твой рейтинг: 98/100")
                    else:
                        st.warning(f"⚠️ Рискованно! '{variant}' помогло лишь частично. Твой рейтинг: 65/100")

# ----------------- 6. ПОДПИСКА -----------------
elif st.session_state.active_tab == "Подписка":
    st.header("💎 Выбери свой уровень доступа")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="pricing-card"><h3>🐣 Free</h3><div class="price-val">0 ₸</div><p>Базовые курсы<br>Лента новостей</p></div>',
            unsafe_allow_html=True)
        if st.button("Активировать Free", use_container_width=True):
            st.success("Бесплатный доступ открыт!")
    with c2:
        st.markdown(
            '<div class="pricing-card" style="border: 2px solid #007bff;"><h3>🚀 PRO</h3><div class="price-val">15 000 ₸</div><p>Все курсы<br>ИИ-наставник 24/7</p></div>',
            unsafe_allow_html=True)
        if st.button("Купить PRO", use_container_width=True):
            with st.expander("Оплата PRO"):
                st.text_input("Номер карты", placeholder="0000 0000 0000 0000")
                col1, col2 = st.columns(2)
                col1.text_input("ММ/ГГ", placeholder="12/28")
                col2.text_input("CVC", type="password", placeholder="***")
                if st.button("Оплатить PRO"):
                    st.success("Оплата PRO успешна! 🎉")
                    st.balloons()
    with c3:
        st.markdown(
            '<div class="pricing-card"><h3>👑 VIP</h3><div class="price-val">30 000 ₸</div><p>Личные консультации<br>Трудоустройство</p></div>',
            unsafe_allow_html=True)
        if st.button("Купить VIP", use_container_width=True):
            with st.expander("Оплата VIP"):
                st.text_input("Номер карты", placeholder="0000 0000 0000 0000")
                col1, col2 = st.columns(2)
                col1.text_input("ММ/ГГ", placeholder="12/28")
                col2.text_input("CVC", type="password", placeholder="***")
                if st.button("Оплатить VIP"):
                    st.success("Оплата VIP успешна! 🎉")
                    st.balloons()
    st.markdown("<hr>", unsafe_allow_html=True)
    st.info("По вопросам корпоративного обучения: nagibator@gmail.com")


# ----------------- КАРТОЧКА ИИ-АССИСТЕНТА -----------------
def render_ai_card():
    # Контейнер всей карточки
    st.markdown("""
        <div style="background: white; padding: 2px; border-radius: 25px; border: 1px solid #e0e0e0; box-shadow: 0 10px 30px rgba(0,0,0,0.08); margin-top: 20px;">
            <div style="background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%); padding: 15px 25px; border-radius: 23px 23px 5px 5px; display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <span style="font-size: 30px;">🤖</span>
                    <div>
                        <h3 style="margin: 0; color: white; font-size: 18px;">EduAI Assistant</h3>
                        <div style="display: flex; align-items: center; gap: 6px;">
                            <div style="width: 8px; height: 8px; background: #00ff00; border-radius: 50%; box-shadow: 0 0 10px #00ff00;"></div>
                            <small style="color: rgba(255,255,255,0.8);">Система активна (Gemini 2.0)</small>
                        </div>
                    </div>
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 5px 12px; border-radius: 10px; color: white; font-size: 12px;">v2.4</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Внутренняя область чата
    chat_inner = st.container(border=False)

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant",
                                      "content": "Привет! Я твой наставник. Могу составить план обучения или объяснить сложную тему. С чего начнем?"}]

    with st.container(height=350, border=False):
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

    # Быстрые команды (кнопки под чатом)
    st.write("⚡ **Быстрые вопросы:**")
    c1, c2, c3 = st.columns(3)
    if c1.button("📚 План на неделю", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Составь мне план обучения на неделю"})
        st.rerun()
    if c2.button("🚀 Взлом карьеры", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Как быстрее всего стать Senior?"})
        st.rerun()
    if c3.button("🧠 Мини-тест", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Проведи короткий квиз по IT"})
        st.rerun()

    # Поле ввода
    if prompt := st.chat_input("Напиши сообщение..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Генерация ответа (имитация)
        with st.spinner("ИИ думает..."):
            time.sleep(1)
            response = f"Анализирую твой запрос: '{prompt}'. В 2026 году это решается через интеграцию нейросетей и системного подхода. Рекомендую изучить документацию в нашей библиотеке!"
            st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()


# Вызов функции на главной или в другом табе
if st.session_state.active_tab == "Главная":
    # Твой остальной код главной страницы...
    st.write("---")
    render_ai_card()