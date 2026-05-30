SELECT eventmodel.id, eventmodel.time, eventmodel.page, eventmodel.description, eventmodel.updated_at 
FROM eventmodel ORDER BY eventmodel.updated_at DESC
LIMIT 10