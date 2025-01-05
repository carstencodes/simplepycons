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


class LightningIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lightning"

    @property
    def original_file_name(self) -> "str":
        return "lightning.svg"

    @property
    def title(self) -> "str":
        return "Lightning"

    @property
    def primary_color(self) -> "str":
        return "#792EE5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lightning</title>
     <path d="M12 0L1.75 6v12L12 24l10.25-6V6zm-1.775
 18l1.08-4.657-2.428-2.397L13.79 6l-1.082 4.665 2.414 2.384z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Lightning-AI/lightning/blo
b/a584196abf820179adb0758ef67ddae91c44e7bc/docs/source/_static/images/'''

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
