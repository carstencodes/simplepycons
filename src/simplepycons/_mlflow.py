#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class MlflowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mlflow"

    @property
    def original_file_name(self) -> "str":
        return "mlflow.svg"

    @property
    def title(self) -> "str":
        return "MLflow"

    @property
    def primary_color(self) -> "str":
        return "#0194E2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MLflow</title>
     <path d="M11.883.002a12.044 12.044 0 0 0-9.326
 19.463l3.668-2.694A7.573 7.573 0 0 1 12.043
 4.45v2.867l6.908-5.14A12.012 12.012 0 0 0 11.883.002zm9.562
 4.533L17.777 7.23a7.573 7.573 0 0 1-5.818 12.322v-2.867l-6.908
 5.14a12.046 12.046 0 0 0 16.394-17.29z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mlflow/mlflow/blob/855881f'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
