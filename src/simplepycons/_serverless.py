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


class ServerlessIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "serverless"

    @property
    def original_file_name(self) -> "str":
        return "serverless.svg"

    @property
    def title(self) -> "str":
        return "Serverless"

    @property
    def primary_color(self) -> "str":
        return "#FD5750"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Serverless</title>
     <path d="M0 17.57h4.248l-1.316 3.974H0zm0-7.557h6.75l-1.316
 3.974H0zm0-7.557h9.252L7.936 6.431H0zm13.44 0H24v3.975H12.123zM9.62
 13.987l1.317-3.974H24v3.974zM8.436 17.57H24v3.975H7.119Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
