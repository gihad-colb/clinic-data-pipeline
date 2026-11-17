SELECT
    clinic,
    COUNT(DISTINCT doctor) AS total_doctors
FROM clinic_schedules
GROUP BY clinic
ORDER BY total_doctors DESC;