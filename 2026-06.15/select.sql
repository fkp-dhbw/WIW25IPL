-- Berechnete Felder, Bedingungen, Sortierung und Gruppierung in SELECT-Anfragen

SELECT
    `Vorname`,
    `Nachname`,
    CONCAT(`Vorname`, ' ', `Nachname`) AS 'Anrede',
    `Geburtsdatum`,
    2025-YEAR(`Geburtsdatum`) as 'Alter',
    `Ort`
FROM
    `Mitarbeiter`
WHERE
	(`AbtID`='EK'
    or `AbtID`='VK')
    and `Ort`='München'
ORDER BY
	`Nachname` DESC;


-- Group By und Aggregatfunktionen
SELECT
	`AbtID`,
    count(*)
FROM
    `Mitarbeiter`
GROUP BY
	`AbtID`;

-- Joins
SELECT 
	*
FROM
	`Mitarbeiter`,
    `Abteilung`
WHERE
	`Mitarbeiter`.`AbtID` = `Abteilung`.`AbtID`;

SELECT
    *
FROM
    `Mitarbeiter`
INNER JOIN `Abteilung` ON `Mitarbeiter`.`AbtID` = `Abteilung`.`AbtID`;

-- Subselects

SELECT
    *
FROM
    `Mitarbeiter`
WHERE
    (
    SELECT
        `Gebaeude`
    FROM
        `Abteilung`
    WHERE
        `Mitarbeiter`.`AbtID` = `Abteilung`.`AbtID`
	) = 'Verwaltung';

SELECT
    *,
    (
    SELECT
        COUNT(*)
    FROM
        `Mitarbeiter`
    WHERE
        `Mitarbeiter`.`AbtID` = `Abteilung`.`AbtID`
	) as 'Anzahl Mitarbeiter'
FROM
    `Abteilung`;