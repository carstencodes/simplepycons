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


class OpsgenieIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opsgenie"

    @property
    def original_file_name(self) -> "str":
        return "opsgenie.svg"

    @property
    def title(self) -> "str":
        return "Opsgenie"

    @property
    def primary_color(self) -> "str":
        return "#172B4D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Opsgenie</title>
     <path d="M12.002 0a5.988 5.988 0 1 1 0 11.975 5.988 5.988 0 0 1
 0-11.975zm9.723 13.026h-.03l-4.527-2.242a.671.671 0 0 0-.876.268
 22.408 22.408 0 0 1-4.306 5.217 22.407 22.407 0 0 1-4.286-5.2.671.671
 0 0 0-.876-.269l-4.535 2.226h-.03a.671.671 0 0 0-.248.902 28.85 28.85
 0 0 0 4.55 5.933l-.002.001c.024.025.05.048.075.072.335.335.676.664
 1.027.981.081.074.165.144.247.217.315.278.632.555.96.82.144.117.295.227.441.341.277.216.552.434.837.639.44.318.888.625
 1.346.917a.963.963 0 0 0 1.007.017c.487-.312.962-.64
 1.428-.98.068-.05.132-.103.2-.153.358-.266.713-.537
 1.06-.82.234-.19.46-.39.688-.588.17-.147.34-.291.506-.442.295-.268.58-.545.864-.825.061-.06.127-.118.188-.179l-.004-.002a28.852
 28.852 0 0 0 4.565-5.949.671.671 0 0 0-.269-.902z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.atlassian.com/company/news/press-'''

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
