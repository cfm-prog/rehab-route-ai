import streamlit as st


st.set_page_config(
    page_title="Нейросетевая маршрутизация реабилитации",
    page_icon="🩺",
    layout="wide",
)


st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem;
        max-width: 1180px;
    }
    h1, h2, h3 {
        color: #102A43;
    }
    .hero {
        padding: 36px 40px;
        border-radius: 18px;
        background: linear-gradient(135deg, #102A43 0%, #1C5D99 100%);
        color: white;
        margin-bottom: 26px;
    }
    .hero h1 {
        color: white;
        font-size: 42px;
        line-height: 1.12;
        margin-bottom: 18px;
    }
    .hero p {
        font-size: 19px;
        line-height: 1.5;
        color: #E6EEF8;
        max-width: 980px;
    }
    .pill {
        display: inline-block;
        padding: 8px 13px;
        margin: 0 8px 8px 0;
        border-radius: 999px;
        background: rgba(255,255,255,0.13);
        color: #FFFFFF;
        font-size: 14px;
    }
    .section-card {
        padding: 22px 24px;
        border: 1px solid #D9E2EF;
        border-radius: 14px;
        background: white;
        height: 100%;
    }
    .metric-card {
        padding: 18px 20px;
        border-left: 6px solid #1C7ED6;
        border-radius: 12px;
        background: #F7FAFE;
        min-height: 112px;
    }
    .metric-card strong {
        display: block;
        font-size: 28px;
        color: #102A43;
        margin-bottom: 6px;
    }
    .small-muted {
        color: #627D98;
        font-size: 14px;
    }
    .footer-note {
        color: #627D98;
        font-size: 14px;
        padding-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="hero">
        <span class="pill">Медицинская реабилитация</span>
        <span class="pill">СППР</span>
        <span class="pill">Нейросетевой алгоритм</span>
        <span class="pill">Пилот в МГТУ</span>
        <h1>Нейросетевой алгоритм поддержки маршрутизации пациентов в медицинской реабилитации</h1>
        <p>
            Цифровой модуль помогает врачу связать исходное состояние пациента, функциональный дефицит,
            выбранное вмешательство, шкалу эффективности и следующий шаг маршрута. Цель проекта -
            перейти от фиксации оказанной услуги к управлению измеримым функциональным результатом.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


left, right = st.columns([1.15, 0.85], gap="large")

with left:
    st.subheader("Проблема")
    st.markdown(
        """
        В реабилитации пациент может пройти курс или этап восстановления, но данные о динамике состояния,
        эффективности вмешательства и необходимости следующего шага часто остаются фрагментарными.

        Для частных клиник и реабилитационных центров это влияет не только на клинический результат,
        но и на экономику: важно показать пациенту результат, удержать его в корректном маршруте,
        снизить лишние повторные обращения и прозрачнее использовать ресурсы.
        """
    )

with right:
    st.subheader("Что предлагаем")
    st.markdown(
        """
        **Цифровой модуль СППР**, который включает:

        - цифровой маршрутный лист;
        - базу стандартизированных случаев;
        - аналитику функциональных исходов;
        - тестовый нейросетевой алгоритм;
        - подготовку к совместимости с МИС и ЕМИАС-подобным контуром.
        """
    )


st.divider()

st.subheader("Как работает маршрутная логика")
cols = st.columns(4)
steps = [
    ("1", "Данные пациента", "Нозология, функциональный дефицит, этап реабилитации."),
    ("2", "Вмешательство", "Цель, технология, параметры курса, противопоказания."),
    ("3", "Результат", "Шкала эффективности, динамика функции, переносимость."),
    ("4", "Решение", "Продолжить, изменить, перевести на этап или завершить реабилитацию."),
]

for col, (num, title, body) in zip(cols, steps):
    with col:
        st.markdown(
            f"""
            <div class="section-card">
                <div class="small-muted">Этап {num}</div>
                <h3>{title}</h3>
                <p>{body}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


st.divider()

pilot_col, plan_col = st.columns([0.95, 1.05], gap="large")

with pilot_col:
    st.subheader("Пилотный план")
    st.markdown(
        """
        **Октябрь:** запуск подготовительного этапа в МГТУ, опрос врачей, определение актуальных
        нозологических групп.

        **Ноябрь - декабрь:** корректировка алгоритма маршрутизации, выбор шкал и структуры данных.

        **Январь - февраль:** прототип цифрового маршрутного листа и первичного модуля аналитики.

        **Март - апрель:** тестовый сбор стандартизированных клинических случаев.

        **Май - июнь:** запуск тестовой версии нейросетевого алгоритма и расчет экономической эффективности.
        """
    )

with plan_col:
    st.subheader("Зачем финансирование")
    st.markdown(
        """
        Первичную проверку идеи можно выполнить на базе МГТУ. Финансирование нужно для перехода
        от исследовательской гипотезы к технологическому продукту:

        - защищенная база данных обезличенных случаев;
        - серверная инфраструктура и резервное хранение;
        - вычислительный контур для тестирования модели;
        - доработка MVP до пилотной версии;
        - подготовка интеграции с МИС и ЕМИАС-подобным контуром.
        """
    )


st.divider()

st.subheader("Расчетная экономика пилота")
calc_left, calc_right = st.columns([0.9, 1.1], gap="large")

with calc_left:
    patients = st.slider("Пациентов в пилоте", min_value=50, max_value=500, value=100, step=10)
    minutes_saved = st.slider("Экономия времени на пациента, минут", min_value=5, max_value=45, value=20, step=5)
    repeat_visit_reduction = st.slider("Предотвращенные лишние визиты, %", min_value=5, max_value=30, value=12, step=1)

hours_saved = patients * minutes_saved / 60
visits_prevented = round(patients * repeat_visit_reduction / 100)

with calc_right:
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(
            f"""<div class="metric-card"><strong>{patients}</strong>пациентов в пилоте</div>""",
            unsafe_allow_html=True,
        )
    with m2:
        st.markdown(
            f"""<div class="metric-card"><strong>{hours_saved:.0f} ч</strong>экономии времени специалистов</div>""",
            unsafe_allow_html=True,
        )
    with m3:
        st.markdown(
            f"""<div class="metric-card"><strong>{visits_prevented}</strong>потенциально предотвращенных лишних визитов</div>""",
            unsafe_allow_html=True,
        )
    st.caption(
        "Расчет является модельной оценкой для пилота. Он нужен для обсуждения гипотезы экономической эффективности с клиниками и инвесторами."
    )


st.divider()

st.subheader("Коммерческая модель")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        """
        **Частные клиники**

        Годовая лицензия, абонентское сопровождение или оплата за пользовательские места и пациентские маршруты.
        """
    )
with c2:
    st.markdown(
        """
        **Реабилитационные центры**

        Пилотное внедрение цифрового маршрутного листа, аналитики и отчета по функциональным исходам.
        """
    )
with c3:
    st.markdown(
        """
        **МИС и партнеры**

        Встраиваемый модуль или white-label решение с подготовкой архитектуры к ЕМИАС-подобному контуру.
        """
    )


st.divider()

with st.form("pilot_form"):
    st.subheader("Заявка на пилот или обсуждение")
    name = st.text_input("Организация / контактное лицо")
    role = st.text_input("Роль или должность")
    comment = st.text_area("Что интересно проверить в пилоте")
    submitted = st.form_submit_button("Сформировать заявку")

if submitted:
    st.success("Заявка сформирована как черновик. Для реального сбора заявок можно подключить Google Forms, email или базу данных.")
    st.write(
        {
            "Организация / контакт": name,
            "Роль": role,
            "Комментарий": comment,
        }
    )


st.markdown(
    """
    <div class="footer-note">
        Проект находится на предпилотной стадии. Алгоритм рассматривается как инструмент поддержки врача,
        а не как замена клинического решения.
    </div>
    """,
    unsafe_allow_html=True,
)
