{{- define "fast-api.postgresHost" -}}
{{ printf "%s-postgresql" .Release.Name }}
{{- end -}}