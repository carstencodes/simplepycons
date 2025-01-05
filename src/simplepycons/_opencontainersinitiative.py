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


class OpenContainersInitiativeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opencontainersinitiative"

    @property
    def original_file_name(self) -> "str":
        return "opencontainersinitiative.svg"

    @property
    def title(self) -> "str":
        return "Open Containers Initiative"

    @property
    def primary_color(self) -> "str":
        return "#262261"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Open Containers Initiative</title>
     <path d="M0 0v24h24V0zm20.547
 20.431H3.448V3.573h17.104V20.43zm-5.155-9.979h3.436v8.255h-3.436zm0-5.16h3.436v3.436h-3.436zm-6.789
 9.976V8.732h5.074v-3.44H5.164v13.415h8.513v-3.44Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/opencontainers/artwork/blo
b/d8ccfe94471a0236b1d4a3f0f90862c4fe5486ce/oci/icon/black/oci-icon-bla'''

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
