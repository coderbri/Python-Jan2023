# Dojos and Ninjas ERD

The **Dojos and Ninjas Schema** is a database of students and the Dojo location at which they're enrolled. The ERD model below demonstrates the **One-to-Many** relationship to represent an application that tracks dojos, as well as the ninjas that belong to each dojo location.

<div align="center">
<img src="./imgs/ERD-Model-DojosNinjas.jpg" width="450px" height="auto">
</div>

The **dojos** table contains the columns of `id`, `name`, `created_at` and `updated_at` whereas the **ninjas** table consists of an `id`, `first_name`, `last_name`, `age`, `created_at`, `updated_at` and belong to a specific dojo (`dojo_id`). MySQL Workbench was used to create the ERD model.

<div align="center">
<img src="./imgs/table-dojos.jpg" width="450px" height="auto">
</div>

<div align="center">
<img src="./imgs/table-ninjas.jpg" width="450px" height="auto">
</div>

**Note:** When any relationship is present, the ON DELETE functionality must be set to **"CASCADE"** so that when the foreign key is deleted, the data linked from the may-to-one relationship is also terminated. See [this project](../015-Books-ERD/) for more details on this.

---
<p align="right">Completed: ２０２３年１０月１３日（金）</p>