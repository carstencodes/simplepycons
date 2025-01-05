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


class PytestIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pytest"

    @property
    def original_file_name(self) -> "str":
        return "pytest.svg"

    @property
    def title(self) -> "str":
        return "Pytest"

    @property
    def primary_color(self) -> "str":
        return "#0A9EDC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pytest</title>
     <path d="M2.6152 0v.8867h3.8399V0zm5.0215 0v.8867h3.8418V0zm4.957
 0v.8867h3.8418V0zm4.9356 0v.8867h3.8418V0zM2.4473 1.8945a.935.935 0 0
 0-.9356.9356c0 .517.4185.9375.9356.9375h19.1054c.5171 0
 .9356-.4204.9356-.9375a.935.935 0 0 0-.9356-.9356zm.168
 2.8477V24H6.455V4.7422zm5.0214 0V20.543h3.8418V4.7422zm4.957
 0V15.291h3.8497V4.7422zm4.9356 0v6.4941h3.8418V4.7422z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/pytest-dev/design/blob/081'''

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
