#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass
from datetime import datetime
from gql.gql.datetime_utils import DATETIME_FIELD
from gql.gql.graphql_client import GraphqlClient
from gql.gql.client import OperationException
from gql.gql.reporter import FailedOperationException
from functools import partial
from numbers import Number
from typing import Any, Callable, List, Mapping, Optional
from time import perf_counter
from dataclasses_json import DataClassJsonMixin

from ..fragment.location import LocationFragment, QUERY as LocationFragmentQuery

QUERY: List[str] = LocationFragmentQuery + ["""
query LocationTypeLocationsQuery($id: ID!) {
  locationType: node(id: $id) {
    ... on LocationType {
      locations {
        edges {
          node {
            ...LocationFragment
          }
        }
      }
    }
  }
}

"""]

@dataclass
class LocationTypeLocationsQuery(DataClassJsonMixin):
    @dataclass
    class LocationTypeLocationsQueryData(DataClassJsonMixin):
        @dataclass
        class Node(DataClassJsonMixin):
            @dataclass
            class LocationConnection(DataClassJsonMixin):
                @dataclass
                class LocationEdge(DataClassJsonMixin):
                    @dataclass
                    class Location(LocationFragment):
                        pass

                    node: Optional[Location]

                edges: List[LocationEdge]

            locations: Optional[LocationConnection]

        locationType: Optional[Node]

    data: LocationTypeLocationsQueryData

    @classmethod
    # fmt: off
    def execute(cls, client: GraphqlClient, id: str) -> Optional[LocationTypeLocationsQueryData.Node]:
        # fmt: off
        variables = {"id": id}
        try:
            network_start = perf_counter()
            response_text = client.call(''.join(set(QUERY)), variables=variables)
            decode_start = perf_counter()
            res = cls.from_json(response_text).data
            decode_time = perf_counter() - decode_start
            network_time = decode_start - network_start
            client.reporter.log_successful_operation("LocationTypeLocationsQuery", variables, network_time, decode_time)
            return res.locationType
        except OperationException as e:
            raise FailedOperationException(
                client.reporter,
                e.err_msg,
                e.err_id,
                "LocationTypeLocationsQuery",
                variables,
            )