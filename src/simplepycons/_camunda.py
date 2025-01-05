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


class CamundaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "camunda"

    @property
    def original_file_name(self) -> "str":
        return "camunda.svg"

    @property
    def title(self) -> "str":
        return "Camunda"

    @property
    def primary_color(self) -> "str":
        return "#FC5D0D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Camunda</title>
     <path d="M3.327 0A3.327 3.327 0 0 0 0 3.326v17.348A3.327 3.327 0
 0 0 3.327 24h17.347A3.326 3.326 0 0 0 24 20.674V3.326A3.326 3.326 0 0
 0 20.674 0H3.327Zm8.687 3.307c1.875 0 2.84 1.105 2.84
 3.049v1.175H13.05V6.23c0-.867-.392-1.203-.994-1.203-.615-.014-.993.322-.993
 1.189v6.56c0 .867.392 1.175.993 1.175.616 0
 .994-.308.994-1.175v-1.734h1.804v1.608c-.014 1.945-.979 3.049-2.854
 3.049-1.874 0-2.839-1.119-2.839-3.035V6.356c.014-1.944.979-3.049
 2.853-3.049ZM9.161 17.476h5.693v3.217H9.161v-3.217Z" />
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
