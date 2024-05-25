#!/usr/bin/env python3

import connexion

from swagger_server import encoder

from swagger_server.utils import setting_statsd, StatsdMiddleware

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Book Reader API'}, pythonic_params=True)

    resource = Resource(attributes={"service.name": "flask-monitoring"})
    tracer = TracerProvider(resource=resource)
    trace.set_tracer_provider(tracer)
    tracer.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint="http://tempo:4317")))

    LoggingInstrumentor().instrument()
    FlaskInstrumentor.instrument_app(app.app, tracer_provider=tracer)

    # Setting statsd host and port
    setting_statsd()
    # Add statsd middleware to track each request and send statsd UDP request
    app.app.wsgi_app = StatsdMiddleware(app.app.wsgi_app, "flask-monitoring")
    
    app.run(port=8000)

if __name__ == '__main__':
    main()
