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


class QuarkusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "quarkus"

    @property
    def original_file_name(self) -> "str":
        return "quarkus.svg"

    @property
    def title(self) -> "str":
        return "Quarkus"

    @property
    def primary_color(self) -> "str":
        return "#4695EB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Quarkus</title>
     <path d="M3.981 0A3.993 3.993 0 0 0 0 3.981V20.02A3.993 3.993 0 0
 0 3.981 24h10.983L12 16.8l-2.15 4.546H3.98c-.72
 0-1.327-.608-1.327-1.327V3.98c0-.72.608-1.327 1.327-1.327h16.04c.72 0
 1.327.608 1.327 1.327v16.04c0 .72-.608 1.327-1.327 1.327h-3.48L17.63
 24h2.388A3.993 3.993 0 0 0 24 20.019V3.98A3.993 3.993 0 0 0 20.019
 0zm4.324 4.217v3.858l3.341-1.93zm7.39 0l-3.341 1.929 3.34 1.929zM12
 6.35L8.305 8.483 12 10.617l3.695-2.134zM8.104 8.832v4.266l3.695
 2.133v-4.266zm7.792 0L12.2 10.965v4.266l3.695-2.133zm-8.146.204l-3.34
 1.93 3.34 1.928zm8.5 0v3.858l3.34-1.929zm-8.146
 4.47v3.859l3.341-1.93zm7.792 0l-3.341 1.93 3.34 1.929z" />
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
